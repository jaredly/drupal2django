#!/usr/bin/env python2.6

import datetime
import random
import string
import time
import os
import imp
from django.core.management import setup_environ
from django.core import serializers

from html2rst.parse import convert_html

cleanup = []

def setup(filename):
    clear_django()
    folder = os.path.dirname(filename)
    name = os.path.basename(filename).split('.')[0]
    fp, filen, desc = imp.find_module(name, [folder])
    try:
        mod = imp.load_module(name, fp, filen, desc)
    finally:
        if fp:
            fp.close()
    setup_environ(mod)
    from django.conf import settings
    settings._setup()

def clear_db():
    from basic.blog.models import Post
    from django.contrib.redirects.models import Redirect
    Post.objects.all().delete()
    Redirect.objects.all().delete()

def drupal_node_to_django(node, revision, slug, user):
    from basic.blog.models import Post
    dct = {'slug':slug,'title':node.title}
    text,skipped = convert_html(revision.body)
    stext, sk2 = convert_html(revision.teaser)
    if skipped or sk2:
        print 'Body not totally parsed', node.title
        text = revision.body
        stext = revision.teaser
        dct['format'] = 'html'
    else:
        dct['format'] = 'rest'
    dct['body'] = text
    dct['tease'] = stext
    dct['status'] = node.status + 1
    dct['created'] = makedtime(node.created)
    dct['publish'] = makedtime(node.changed)
    dct['modified'] = makedtime(node.changed)
    dct['allow_comments'] = node.comment == 2
    dct['author'] = user
    # no tags, categories, objects, or author yet.
    post = Post(**dct)
    return post

def migrate(drupals, djangos):
    setup(drupals)

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from drupal2django.models import Users, Node, NodeRevisions, UrlAlias
    sys.path.pop(0)

    nodes = get_nodes(Node, NodeRevisions)
    users = Users.objects.all()

    urls = list(UrlAlias.objects.all())

    setup(djangos)
    from django.conf import settings
    clear_db()

    django_save_users(users)
    django_save_nodes(nodes, users, urls)

def django_save_users(users):
    from django.contrib.auth.models import User
    current = set(u.username for u in User.objects.all())
    for user in users:
        if not user.name:continue
        if user.name in current:
            # print 'Skipping import or %s: name conflict' % user.name
            continue
        dct = {'username':user.name, 'email':user.mail, 'password':user.pass_field,
                'last_login':makedtime(user.login),
                'date_joined':makedtime(user.created)}
        print 'saving',user.name
        User(**dct).save()

def django_save_nodes(nodes, users, urls):
    from django.contrib.auth.models import User
    url_dict = dict((url.src,url) for url in urls)
    user_dict = dict((user.uid,user.name) for user in users)
    for node, revision in nodes:
        path = url_dict.get('node/%d' % node.nid, None)
        if not path:
            slug = node.title.replace(' ','-').replace('/','-')
        else:
            slug = path.dst.split('/')[-1]
        
        user = User.objects.get(username=user_dict[node.uid])

        post = drupal_node_to_django(node, revision, slug, user)
        post.save()
        drupal_redirect_django(path, post)
    

def get_nodes(Node, NodeRevisions):
    nodes = []
    for node in Node.objects.all().filter(type="blog"):
        recent = NodeRevisions.objects.all().filter(nid=node.nid).order_by('-timestamp')[0]
        nodes.append([node,recent])
    return nodes

def drupal_redirect_django(path, post):
    from django.contrib.redirects.models import Redirect
    from django.contrib.sites.models import Site
    current = Site.objects.get_current()
    if path:
        dst = '/' + path.dst.strip('/') + '/'
        r = Redirect(site=current, old_path=dst, new_path='/example'+post.get_absolute_url())
        r.save()
        src = '/' + path.src.strip('/') + '/'
        r = Redirect(site=current, old_path=src, new_path='/example'+post.get_absolute_url())
        r.save()

def makedtime(secs):
    return datetime.datetime(*time.localtime(secs)[:-3])

def clear_django():
    for name in sys.modules.keys():
        if name == 'django' or name.startswith('django.'):
            del sys.modules[name]
    import django

if __name__=='__main__':
    import sys
    drupals, djangos = sys.argv[1:]
    migrate(drupals, djangos)

# vim: et sw=4 sts=4
