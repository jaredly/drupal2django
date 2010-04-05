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
    folder = os.path.dirname(filename)
    name = os.path.basename(filename).split('.')[0]
    fp, filen, desc = imp.find_module(name, [folder])
    try:
        mod = imp.load_module(name, fp, filen, desc)
    finally:
        if fp:
            fp.close()
    setup_environ(mod)

def setup_hack(dct):
    fname = rfilename()
    open(fname+'.py','w').write('''
DATABASE_ENGINE = '%s'
DATABASE_NAME = '%s'
DATABASE_USER = '%s'
DATABASE_PASSWORD = '%s'
''' % (dct['engine'], dct.get('name',''), dct.get('user',''), dct.get('pass','')))
    settings = __import__(fname)

    setup_environ(settings)
    os.remove(fname+'.py')
    cleanup.append(fname+'.pyc')

def migrate(drupals, djangos):
    setup(drupals)

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from drupal2django.models import Node, NodeRevisions, UrlAlias
    sys.path.pop(0)
    nodes = []
    for node in Node.objects.all().filter(type="blog"):
        recent = NodeRevisions.objects.all().filter(nid=node.nid).order_by('-timestamp')[0]
        nodes.append([node,recent])
    urls = list(UrlAlias.objects.all())
    url_dict = dict((url.src,url) for url in urls)

    clear_django()

    setup(djangos)
    from basic.blog.models import Post
    from django.contrib.redirects.models import Redirect
    from django.conf import settings
    from django.contrib.sites.models import Site
    Post.objects.all().delete()
    Redirect.objects.all().delete()
    posts = list(Post.objects.all())

    for node, revision in nodes:
        path = url_dict.get('node/%d' % node.nid, None)
        if not path:
            print 'no path',node.nid, node.title
            slug = node.title.replace(' ','-').replace('/','-')
        else:
            slug = path.dst.split('/')[-1]
        dct = {'slug':slug,'title':node.title}
        # TODO add user conversion
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
        # no tags, categories, objects, or author yet.
        post = Post(**dct)
        post.save()
        post.created = makedtime(node.created)
        post.publish = makedtime(node.changed)
        post.modified = makedtime(node.changed)
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
