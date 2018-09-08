name 'chef_exercicio'
maintainer 'The Authors'
maintainer_email 'you@example.com'
license 'All Rights Reserved'
description 'Installs/Configures chef_exercicio'
long_description 'Installs/Configures chef_exercicio'
version '0.4.2'
chef_version '>= 12.14' if respond_to?(:chef_version)

depends 'sudo', '~> 5.4.2'
depends 'system', '~> 0.11.3'

# The `issues_url` points to the location where issues for this cookbook are
# tracked.  A `View Issues` link will be displayed on this cookbook's page when
# uploaded to a Supermarket.
#
# issues_url 'https://github.com/<insert_org_here>/chef_exercicio/issues'

# The `source_url` points to the development repository for this cookbook.  A
# `View Source` link will be displayed on this cookbook's page when uploaded to
# a Supermarket.
#
# source_url 'https://github.com/<insert_org_here>/chef_exercicio'
