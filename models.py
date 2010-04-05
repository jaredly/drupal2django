#!/usr/bin/env python
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
'''
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
'''

# vim: et sw=4 sts=4
