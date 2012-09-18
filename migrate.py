#!/usr/bin/env python2.6
'''Copyright (c) 2010-2012 Jared Forsyth

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''


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

def drupal_node_to_django(node, revision, slug, user, drupal_root):
    from basic.blog.models import Post
    from django.conf import settings
    dct = {'slug':slug,'title':node.title}
    rest = convert_html(revision.body, media_root=settings.MEDIA_ROOT, drupal_root=drupal_root, media_url=settings.MEDIA_URL)
    rest2 = convert_html(revision.teaser, media_root=settings.MEDIA_ROOT, drupal_root=drupal_root, media_url=settings.MEDIA_URL)
    if rest.skipped or rest2.skipped:
        print 'Body not totally parsed', node.title
        text = revision.body
        stext = revision.teaser
        dct['format'] = 'html'
    else:
        dct['format'] = 'rest'

    dct['body'] = rest.rest
    dct['tease'] = rest2.rest
    dct['status'] = node.status + 1
    dct['created'] = makedtime(node.created)
    dct['publish'] = makedtime(node.changed)
    dct['modified'] = makedtime(node.changed)
    dct['allow_comments'] = node.comment == 2
    dct['author'] = user
    # no tags, categories, objects, or author yet.
    post = Post(**dct)
    return post, rest.images

def migrate(drupals, djangos):
    setup(drupals)

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from drupal2django.models import Users, Node, NodeRevisions, UrlAlias, Files
    sys.path.pop(0)

    nodes = get_nodes(Node, NodeRevisions)
    print 'nodes:',len(nodes)
    users = Users.objects.all()
    files = Files.objects.all()
    from django.conf import settings
    drupal_root = getattr(settings, 'DRUPAL_ROOT', None)

    urls = list(UrlAlias.objects.all())

    setup(djangos)
    from django.conf import settings
    clear_db()

    django_save_users(users)
    django_save_nodes(nodes, users, urls, drupal_root)

    #django_move_files(files, drupal_root)

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
        User(**dct).save()

def django_save_nodes(nodes, users, urls, drupal_root):
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

        post, images = drupal_node_to_django(node, revision, slug, user, drupal_root)
        post.save()
        drupal_redirect_django(path, post)

def django_move_files(files, root):
    '''move files that drupal knows about to the media folder, and add a redirect for each.
    TODO: make the destination directory configurable, don't die on duplicate names.'''

    from django.contrib.redirects.models import Redirect
    from django.contrib.sites.models import Site
    current = Site.objects.get_current()

    from django.conf import settings
    filedir = os.path.join(settings.MEDIA_ROOT, 'from_drupal')

    if not os.path.exists(filedir):
        os.mkdir(filedir)
    elif not os.path.isdir(filedir):
        raise Exception, '%s exists and is not a directory.' % filedir

    for file in files:
        django_move_file(file.filepath, root, filedir)

def django_move_file(filepath, root):
    name = os.path.basename(filepath)
    realpath = os.path.join(root, filepath)
    nname = os.path.join(filedir, name)
    from django.conf import settings
    if os.path.exists(nname):
        #print 'Duplicate file name. skipping %s (from %s)' % (name, filepath)
        #continue
        pass
    if not os.path.exists(realpath):
        print 'file not found (%s). skipping' % realpath
        return 
    open(nname, 'wb').write(open(realpath, 'rb').read())
    try:
        Redirect(site=current, old_path='/'+filepath+'/', new_path=settings.MEDIA_URL + 'from_drupal/%s' % name).save()
    except:pass
        

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
