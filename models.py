#!/usr/bin/env python
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

from django.db import models

class NodeRevisions(models.Model):
    nid = models.IntegerField()
    vid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    title = models.CharField(max_length=765)
    body = models.TextField()
    teaser = models.TextField()
    log = models.TextField()
    timestamp = models.IntegerField()
    format = models.IntegerField()
    class Meta:
        db_table = u'node_revisions'

class UrlAlias(models.Model):
    pid = models.IntegerField(primary_key=True)
    src = models.CharField(max_length=384)
    dst = models.CharField(unique=True, max_length=384)
    language = models.CharField(unique=True, max_length=36)
    class Meta:
        db_table = u'url_alias'

class TermData(models.Model):
    tid = models.IntegerField(primary_key=True)
    vid = models.IntegerField()
    name = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    weight = models.IntegerField()
    class Meta:
        db_table = u'term_data'

class Node(models.Model):
    nid = models.IntegerField(primary_key=True)
    vid = models.IntegerField(unique=True)
    type = models.CharField(max_length=96)
    language = models.CharField(max_length=36)
    title = models.CharField(max_length=765)
    uid = models.IntegerField()
    status = models.IntegerField()
    created = models.IntegerField()
    changed = models.IntegerField()
    comment = models.IntegerField()
    promote = models.IntegerField()
    moderate = models.IntegerField()
    sticky = models.IntegerField()
    tnid = models.IntegerField()
    translate = models.IntegerField()
    class Meta:
        db_table = u'node'

class TermNode(models.Model):
    nid = models.IntegerField()
    vid = models.IntegerField()
    tid = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'term_node'

class Users(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=180)
    pass_field = models.CharField(max_length=96, db_column='pass') # Field renamed because it was a Python reserved word. Field name made lowercase.
    mail = models.CharField(max_length=192, blank=True)
    mode = models.IntegerField()
    sort = models.IntegerField(null=True, blank=True)
    threshold = models.IntegerField(null=True, blank=True)
    theme = models.CharField(max_length=765)
    signature = models.CharField(max_length=765)
    created = models.IntegerField()
    access = models.IntegerField()
    login = models.IntegerField()
    status = models.IntegerField()
    timezone = models.CharField(max_length=24, blank=True)
    language = models.CharField(max_length=36)
    picture = models.CharField(max_length=765)
    init = models.CharField(max_length=192, blank=True)
    data = models.TextField(blank=True)
    class Meta:
        db_table = u'users'

class Files(models.Model):
    fid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    filename = models.CharField(max_length=765)
    filepath = models.CharField(max_length=765)
    filemime = models.CharField(max_length=765)
    filesize = models.IntegerField()
    status = models.IntegerField()
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'files'

# vim: et sw=4 sts=4
