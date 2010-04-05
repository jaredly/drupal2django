Migrate Drupal to Django
========================

This is an app which migrates a drupal blog to django, with a focus on
minimizing loss -- all old urls are mapped (through contrib.redirect) to the
new posts, so no SEO value is lost.

Works:

- post migration to basic.blog models
- url redirect mapping, both from the /node/# url and whatever extra redirect
  url you had

TODO:

- user migration
- comments migration
- flatpage migration
- menu migration
- more configuration
    * import nodes of more types (not just Post)
    * export to more than just basic.blog
- copy images and linked files
- be aware of CCK fields

