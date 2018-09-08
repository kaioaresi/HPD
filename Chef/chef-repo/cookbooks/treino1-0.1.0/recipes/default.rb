#
# Cookbook:: treino1
# Recipe:: default
#
# Copyright:: 2018, The Authors, All Rights Reserved.

include_recipe "chef-client::config"

package 'nginx'

service 'nginx' do
  action [:enable, :start]
end

file '/usr/share/nginx/html/index.html' do
    content '<h1>Instalado via chef</h1>'
end

puts node.chef_environment


if node.environment == "prod"
    file '/usr/share/nginx/html/index.html' do
      content '<h1>Instalado via chef Ambiente de production</h1>'
    end
end
