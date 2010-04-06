# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Access(models.Model):
    aid = models.IntegerField(primary_key=True)
    mask = models.CharField(max_length=765)
    type = models.CharField(max_length=765)
    status = models.IntegerField()
    class Meta:
        db_table = u'access'

class Accesslog(models.Model):
    aid = models.IntegerField(primary_key=True)
    sid = models.CharField(max_length=192)
    title = models.CharField(max_length=765, blank=True)
    path = models.CharField(max_length=765, blank=True)
    url = models.CharField(max_length=765, blank=True)
    hostname = models.CharField(max_length=384, blank=True)
    uid = models.IntegerField(null=True, blank=True)
    timer = models.IntegerField()
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'accesslog'

class Actions(models.Model):
    aid = models.CharField(max_length=765, primary_key=True)
    type = models.CharField(max_length=96)
    callback = models.CharField(max_length=765)
    parameters = models.TextField()
    description = models.CharField(max_length=765)
    class Meta:
        db_table = u'actions'

class ActionsAid(models.Model):
    aid = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'actions_aid'

class AdvancedHelpIndex(models.Model):
    sid = models.IntegerField(primary_key=True)
    module = models.CharField(max_length=765)
    topic = models.CharField(max_length=765)
    language = models.CharField(max_length=36)
    class Meta:
        db_table = u'advanced_help_index'

class AggregatorCategory(models.Model):
    cid = models.IntegerField(primary_key=True)
    title = models.CharField(unique=True, max_length=765)
    description = models.TextField()
    block = models.IntegerField()
    class Meta:
        db_table = u'aggregator_category'

class AggregatorCategoryFeed(models.Model):
    fid = models.IntegerField()
    cid = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'aggregator_category_feed'

class AggregatorCategoryItem(models.Model):
    iid = models.IntegerField()
    cid = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'aggregator_category_item'

class AggregatorFeed(models.Model):
    fid = models.IntegerField(primary_key=True)
    title = models.CharField(unique=True, max_length=765)
    url = models.CharField(unique=True, max_length=765)
    refresh = models.IntegerField()
    checked = models.IntegerField()
    link = models.CharField(max_length=765)
    description = models.TextField()
    image = models.TextField()
    etag = models.CharField(max_length=765)
    modified = models.IntegerField()
    block = models.IntegerField()
    class Meta:
        db_table = u'aggregator_feed'

class AggregatorItem(models.Model):
    iid = models.IntegerField(primary_key=True)
    fid = models.IntegerField()
    title = models.CharField(max_length=765)
    link = models.CharField(max_length=765)
    author = models.CharField(max_length=765)
    description = models.TextField()
    timestamp = models.IntegerField(null=True, blank=True)
    guid = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'aggregator_item'

class Authmap(models.Model):
    aid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    authname = models.CharField(unique=True, max_length=384)
    module = models.CharField(max_length=384)
    class Meta:
        db_table = u'authmap'

class Batch(models.Model):
    bid = models.IntegerField(primary_key=True)
    token = models.CharField(max_length=192)
    timestamp = models.IntegerField()
    batch = models.TextField(blank=True)
    class Meta:
        db_table = u'batch'

class Blocks(models.Model):
    bid = models.IntegerField(primary_key=True)
    module = models.CharField(max_length=192)
    delta = models.CharField(unique=True, max_length=96)
    theme = models.CharField(max_length=192)
    status = models.IntegerField()
    weight = models.IntegerField()
    region = models.CharField(max_length=192)
    custom = models.IntegerField()
    throttle = models.IntegerField()
    visibility = models.IntegerField()
    pages = models.TextField()
    title = models.CharField(max_length=192)
    cache = models.IntegerField()
    class Meta:
        db_table = u'blocks'

class BlocksRoles(models.Model):
    module = models.CharField(max_length=192, primary_key=True)
    delta = models.CharField(max_length=96, primary_key=True)
    rid = models.IntegerField()
    class Meta:
        db_table = u'blocks_roles'

class BlogapiFiles(models.Model):
    fid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    filepath = models.CharField(max_length=765)
    filesize = models.IntegerField()
    class Meta:
        db_table = u'blogapi_files'

class Boxes(models.Model):
    bid = models.IntegerField(primary_key=True)
    body = models.TextField(blank=True)
    info = models.CharField(unique=True, max_length=384)
    format = models.IntegerField()
    class Meta:
        db_table = u'boxes'

class Cache(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache'

class CacheAdminMenu(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_admin_menu'

class CacheBlock(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_block'

class CacheContent(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_content'

class CacheFilter(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_filter'

class CacheForm(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_form'

class CacheMenu(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_menu'

class CachePage(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_page'

class CacheUpdate(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_update'

class CacheViews(models.Model):
    cid = models.CharField(max_length=765, primary_key=True)
    data = models.TextField(blank=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True)
    serialized = models.IntegerField()
    class Meta:
        db_table = u'cache_views'

class Comments(models.Model):
    cid = models.IntegerField(primary_key=True)
    pid = models.IntegerField()
    nid = models.IntegerField()
    uid = models.IntegerField()
    subject = models.CharField(max_length=192)
    comment = models.TextField()
    hostname = models.CharField(max_length=384)
    timestamp = models.IntegerField()
    status = models.IntegerField()
    format = models.IntegerField()
    thread = models.CharField(max_length=765)
    name = models.CharField(max_length=180, blank=True)
    mail = models.CharField(max_length=192, blank=True)
    homepage = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'comments'

class Contact(models.Model):
    cid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=765)
    recipients = models.TextField()
    reply = models.TextField()
    weight = models.IntegerField()
    selected = models.IntegerField()
    class Meta:
        db_table = u'contact'

class ContentNodeField(models.Model):
    field_name = models.CharField(max_length=96, primary_key=True)
    type = models.CharField(max_length=381)
    global_settings = models.TextField()
    required = models.IntegerField()
    multiple = models.IntegerField()
    db_storage = models.IntegerField()
    module = models.CharField(max_length=381)
    db_columns = models.TextField()
    active = models.IntegerField()
    locked = models.IntegerField()
    class Meta:
        db_table = u'content_node_field'

class ContentNodeFieldInstance(models.Model):
    field_name = models.CharField(max_length=96, primary_key=True)
    type_name = models.CharField(max_length=96, primary_key=True)
    weight = models.IntegerField()
    label = models.CharField(max_length=765)
    widget_type = models.CharField(max_length=96)
    widget_settings = models.TextField()
    display_settings = models.TextField()
    description = models.TextField()
    widget_module = models.CharField(max_length=381)
    widget_active = models.IntegerField()
    class Meta:
        db_table = u'content_node_field_instance'

class ContentTypeProject(models.Model):
    vid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    field_link_url = models.CharField(max_length=765, blank=True)
    field_link_title = models.CharField(max_length=765, blank=True)
    field_link_attributes = models.TextField(blank=True)
    field_source_url = models.CharField(max_length=765, blank=True)
    field_source_title = models.CharField(max_length=765, blank=True)
    field_source_attributes = models.TextField(blank=True)
    class Meta:
        db_table = u'content_type_project'

class DevelQueries(models.Model):
    qid = models.IntegerField()
    function = models.CharField(max_length=765)
    query = models.TextField()
    hash = models.CharField(max_length=765, primary_key=True)
    class Meta:
        db_table = u'devel_queries'

class DevelTimes(models.Model):
    tid = models.IntegerField(primary_key=True)
    qid = models.IntegerField()
    time = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'devel_times'

class Feedburner(models.Model):
    path = models.CharField(max_length=384, primary_key=True)
    feedburner = models.CharField(max_length=300)
    class Meta:
        db_table = u'feedburner'

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

class FilterFormats(models.Model):
    format = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=765)
    roles = models.CharField(max_length=765)
    cache = models.IntegerField()
    class Meta:
        db_table = u'filter_formats'

class Filters(models.Model):
    fid = models.IntegerField(primary_key=True)
    format = models.IntegerField()
    module = models.CharField(max_length=192)
    delta = models.IntegerField()
    weight = models.IntegerField()
    class Meta:
        db_table = u'filters'

class Flood(models.Model):
    fid = models.IntegerField(primary_key=True)
    event = models.CharField(max_length=192)
    hostname = models.CharField(max_length=384)
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'flood'

class History(models.Model):
    uid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'history'

class Image(models.Model):
    nid = models.IntegerField()
    fid = models.IntegerField()
    image_size = models.CharField(max_length=96)
    class Meta:
        db_table = u'image'

class ImageAttach(models.Model):
    nid = models.IntegerField()
    iid = models.IntegerField()
    class Meta:
        db_table = u'image_attach'

class Languages(models.Model):
    language = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=192)
    native = models.CharField(max_length=192)
    direction = models.IntegerField()
    enabled = models.IntegerField()
    plurals = models.IntegerField()
    formula = models.CharField(max_length=384)
    domain = models.CharField(max_length=384)
    prefix = models.CharField(max_length=384)
    weight = models.IntegerField()
    javascript = models.CharField(max_length=96)
    class Meta:
        db_table = u'languages'

class LocalesSource(models.Model):
    lid = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=765)
    textgroup = models.CharField(max_length=765)
    source = models.TextField()
    version = models.CharField(max_length=60)
    class Meta:
        db_table = u'locales_source'

class LocalesTarget(models.Model):
    lid = models.IntegerField()
    translation = models.TextField()
    language = models.CharField(max_length=36, primary_key=True)
    plid = models.IntegerField()
    plural = models.IntegerField()
    class Meta:
        db_table = u'locales_target'

class MenuCustom(models.Model):
    menu_name = models.CharField(max_length=96, primary_key=True)
    title = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'menu_custom'

class MenuLinks(models.Model):
    menu_name = models.CharField(max_length=96)
    mlid = models.IntegerField(primary_key=True)
    plid = models.IntegerField()
    link_path = models.CharField(max_length=765)
    router_path = models.CharField(max_length=765)
    link_title = models.CharField(max_length=765)
    options = models.TextField(blank=True)
    module = models.CharField(max_length=765)
    hidden = models.IntegerField()
    external = models.IntegerField()
    has_children = models.IntegerField()
    expanded = models.IntegerField()
    weight = models.IntegerField()
    depth = models.IntegerField()
    customized = models.IntegerField()
    p1 = models.IntegerField()
    p2 = models.IntegerField()
    p3 = models.IntegerField()
    p4 = models.IntegerField()
    p5 = models.IntegerField()
    p6 = models.IntegerField()
    p7 = models.IntegerField()
    p8 = models.IntegerField()
    p9 = models.IntegerField()
    updated = models.IntegerField()
    class Meta:
        db_table = u'menu_links'

class MenuRouter(models.Model):
    path = models.CharField(max_length=765, primary_key=True)
    load_functions = models.CharField(max_length=765)
    to_arg_functions = models.CharField(max_length=765)
    access_callback = models.CharField(max_length=765)
    access_arguments = models.TextField(blank=True)
    page_callback = models.CharField(max_length=765)
    page_arguments = models.TextField(blank=True)
    fit = models.IntegerField()
    number_parts = models.IntegerField()
    tab_parent = models.CharField(max_length=765)
    tab_root = models.CharField(max_length=765)
    title = models.CharField(max_length=765)
    title_callback = models.CharField(max_length=765)
    title_arguments = models.CharField(max_length=765)
    type = models.IntegerField()
    block_callback = models.CharField(max_length=765)
    description = models.TextField()
    position = models.CharField(max_length=765)
    weight = models.IntegerField()
    file = models.TextField(blank=True)
    class Meta:
        db_table = u'menu_router'

class Node(models.Model):
    nid = models.IntegerField()
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

class NodeAccess(models.Model):
    nid = models.IntegerField(primary_key=True)
    gid = models.IntegerField(primary_key=True)
    realm = models.CharField(max_length=765, primary_key=True)
    grant_view = models.IntegerField()
    grant_update = models.IntegerField()
    grant_delete = models.IntegerField()
    class Meta:
        db_table = u'node_access'

class NodeCommentStatistics(models.Model):
    nid = models.IntegerField(primary_key=True)
    last_comment_timestamp = models.IntegerField()
    last_comment_name = models.CharField(max_length=180, blank=True)
    last_comment_uid = models.IntegerField()
    comment_count = models.IntegerField()
    class Meta:
        db_table = u'node_comment_statistics'

class NodeCounter(models.Model):
    nid = models.IntegerField(primary_key=True)
    totalcount = models.IntegerField()
    daycount = models.IntegerField()
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'node_counter'

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

class NodeType(models.Model):
    type = models.CharField(max_length=96, primary_key=True)
    name = models.CharField(max_length=765)
    module = models.CharField(max_length=765)
    description = models.TextField()
    help = models.TextField()
    has_title = models.IntegerField()
    title_label = models.CharField(max_length=765)
    has_body = models.IntegerField()
    body_label = models.CharField(max_length=765)
    min_word_count = models.IntegerField()
    custom = models.IntegerField()
    modified = models.IntegerField()
    locked = models.IntegerField()
    orig_type = models.CharField(max_length=765)
    class Meta:
        db_table = u'node_type'

class NodewordsAttributes(models.Model):
    attid = models.IntegerField(primary_key=True)
    tagid = models.IntegerField()
    name = models.CharField(max_length=96)
    value = models.CharField(max_length=384)
    weight = models.IntegerField()
    class Meta:
        db_table = u'nodewords_attributes'

class NodewordsContentNode(models.Model):
    tagid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    vid = models.IntegerField(primary_key=True)
    delta = models.IntegerField()
    value = models.TextField()
    class Meta:
        db_table = u'nodewords_content_node'

class NodewordsDefaults(models.Model):
    tagid = models.IntegerField(primary_key=True)
    context = models.CharField(max_length=192, primary_key=True)
    value = models.TextField()
    enabled = models.IntegerField()
    editable = models.IntegerField()
    class Meta:
        db_table = u'nodewords_defaults'

class NodewordsTags(models.Model):
    tagid = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=48)
    name = models.CharField(max_length=96)
    description = models.CharField(max_length=384, blank=True)
    widget = models.CharField(max_length=48)
    widget_options = models.TextField(blank=True)
    options = models.TextField(blank=True)
    weight = models.IntegerField()
    class Meta:
        db_table = u'nodewords_tags'

class PageTitle(models.Model):
    nid = models.IntegerField(primary_key=True)
    page_title = models.CharField(max_length=765)
    class Meta:
        db_table = u'page_title'

class Permission(models.Model):
    pid = models.IntegerField(primary_key=True)
    rid = models.IntegerField()
    perm = models.TextField(blank=True)
    tid = models.IntegerField()
    class Meta:
        db_table = u'permission'

class PluginManagerQueue(models.Model):
    short_name = models.CharField(max_length=765, primary_key=True)
    class Meta:
        db_table = u'plugin_manager_queue'

class PluginManagerRepository(models.Model):
    title = models.CharField(max_length=765)
    short_name = models.CharField(max_length=765, primary_key=True)
    links = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'plugin_manager_repository'

class PluginManagerTaxonomy(models.Model):
    short_name = models.CharField(max_length=765)
    tag = models.CharField(max_length=765)
    class Meta:
        db_table = u'plugin_manager_taxonomy'

class Role(models.Model):
    rid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=192)
    class Meta:
        db_table = u'role'

class SearchDataset(models.Model):
    sid = models.IntegerField(unique=True)
    type = models.CharField(unique=True, max_length=48, blank=True)
    data = models.TextField()
    reindex = models.IntegerField()
    class Meta:
        db_table = u'search_dataset'

class SearchIndex(models.Model):
    word = models.CharField(max_length=150)
    sid = models.IntegerField()
    type = models.CharField(max_length=48, blank=True)
    score = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'search_index'

class SearchNodeLinks(models.Model):
    sid = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=48, primary_key=True)
    nid = models.IntegerField()
    caption = models.TextField(blank=True)
    class Meta:
        db_table = u'search_node_links'

class SearchTotal(models.Model):
    word = models.CharField(max_length=150, primary_key=True)
    count = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'search_total'

class Sessions(models.Model):
    uid = models.IntegerField()
    sid = models.CharField(max_length=192, primary_key=True)
    hostname = models.CharField(max_length=384)
    timestamp = models.IntegerField()
    cache = models.IntegerField()
    session = models.TextField(blank=True)
    class Meta:
        db_table = u'sessions'

class System(models.Model):
    filename = models.CharField(max_length=765)
    name = models.CharField(max_length=765)
    type = models.CharField(max_length=765)
    owner = models.CharField(max_length=765)
    status = models.IntegerField()
    throttle = models.IntegerField()
    bootstrap = models.IntegerField()
    schema_version = models.IntegerField()
    weight = models.IntegerField()
    info = models.TextField(blank=True)
    class Meta:
        db_table = u'system'

class TermData(models.Model):
    tid = models.IntegerField(primary_key=True)
    vid = models.IntegerField()
    name = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    weight = models.IntegerField()
    class Meta:
        db_table = u'term_data'

class TermHierarchy(models.Model):
    tid = models.IntegerField(primary_key=True)
    parent = models.IntegerField()
    class Meta:
        db_table = u'term_hierarchy'

class TermNode(models.Model):
    nid = models.IntegerField()
    vid = models.IntegerField()
    tid = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'term_node'

class TermRelation(models.Model):
    trid = models.IntegerField(primary_key=True)
    tid1 = models.IntegerField(unique=True)
    tid2 = models.IntegerField()
    class Meta:
        db_table = u'term_relation'

class TermSynonym(models.Model):
    tsid = models.IntegerField(primary_key=True)
    tid = models.IntegerField()
    name = models.CharField(max_length=765)
    class Meta:
        db_table = u'term_synonym'

class TinymceRole(models.Model):
    name = models.CharField(max_length=384, primary_key=True)
    rid = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'tinymce_role'

class TinymceSettings(models.Model):
    name = models.CharField(max_length=384, primary_key=True)
    settings = models.TextField(blank=True)
    class Meta:
        db_table = u'tinymce_settings'

class Upload(models.Model):
    fid = models.IntegerField()
    nid = models.IntegerField()
    vid = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=765)
    list = models.IntegerField()
    weight = models.IntegerField()
    class Meta:
        db_table = u'upload'

class UrlAlias(models.Model):
    pid = models.IntegerField(primary_key=True)
    src = models.CharField(max_length=384)
    dst = models.CharField(unique=True, max_length=384)
    language = models.CharField(unique=True, max_length=36)
    class Meta:
        db_table = u'url_alias'

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

class UsersRoles(models.Model):
    uid = models.IntegerField(primary_key=True)
    rid = models.IntegerField()
    class Meta:
        db_table = u'users_roles'

class Variable(models.Model):
    name = models.CharField(max_length=384, primary_key=True)
    value = models.TextField()
    class Meta:
        db_table = u'variable'

class ViewsDisplay(models.Model):
    vid = models.IntegerField()
    id = models.CharField(max_length=192, primary_key=True)
    display_title = models.CharField(max_length=192)
    display_plugin = models.CharField(max_length=192)
    position = models.IntegerField(null=True, blank=True)
    display_options = models.TextField(blank=True)
    class Meta:
        db_table = u'views_display'

class ViewsObjectCache(models.Model):
    sid = models.CharField(max_length=192, blank=True)
    name = models.CharField(max_length=96, blank=True)
    obj = models.CharField(max_length=96, blank=True)
    updated = models.IntegerField()
    data = models.TextField(blank=True)
    class Meta:
        db_table = u'views_object_cache'

class ViewsView(models.Model):
    vid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=96)
    description = models.CharField(max_length=765, blank=True)
    tag = models.CharField(max_length=765, blank=True)
    view_php = models.TextField(blank=True)
    base_table = models.CharField(max_length=96)
    is_cacheable = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'views_view'

class Vocabulary(models.Model):
    vid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    help = models.CharField(max_length=765)
    relations = models.IntegerField()
    hierarchy = models.IntegerField()
    multiple = models.IntegerField()
    required = models.IntegerField()
    tags = models.IntegerField()
    module = models.CharField(max_length=765)
    weight = models.IntegerField()
    class Meta:
        db_table = u'vocabulary'

class VocabularyNodeTypes(models.Model):
    vid = models.IntegerField()
    type = models.CharField(max_length=96, primary_key=True)
    class Meta:
        db_table = u'vocabulary_node_types'

class VotingapiCache(models.Model):
    vote_cache_id = models.IntegerField(primary_key=True)
    content_type = models.CharField(max_length=192)
    content_id = models.IntegerField()
    value = models.FloatField()
    value_type = models.CharField(max_length=192)
    tag = models.CharField(max_length=192)
    function = models.CharField(max_length=192)
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'votingapi_cache'

class VotingapiVote(models.Model):
    vote_id = models.IntegerField(primary_key=True)
    content_type = models.CharField(max_length=192)
    content_id = models.IntegerField()
    value = models.FloatField()
    value_type = models.CharField(max_length=192)
    tag = models.CharField(max_length=192)
    uid = models.IntegerField()
    timestamp = models.IntegerField()
    vote_source = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'votingapi_vote'

class Watchdog(models.Model):
    wid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    type = models.CharField(max_length=48)
    message = models.TextField()
    variables = models.TextField()
    severity = models.IntegerField()
    link = models.CharField(max_length=765)
    location = models.TextField()
    referer = models.CharField(max_length=384)
    hostname = models.CharField(max_length=384)
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'watchdog'

class Weblinks(models.Model):
    nid = models.IntegerField(primary_key=True)
    vid = models.IntegerField(primary_key=True)
    click_count = models.IntegerField()
    last_click = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField()
    last_status = models.CharField(max_length=12, blank=True)
    last_checked = models.IntegerField(null=True, blank=True)
    urlhash = models.CharField(max_length=96)
    url = models.TextField()
    reciprocal = models.TextField(blank=True)
    class Meta:
        db_table = u'weblinks'

