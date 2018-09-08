#
# Cookbook:: chef_exercicio
# Recipe:: default
#
# Copyright:: 2018, The Authors, All Rights Reserved.

include_recipe 'system::default'

if node['os'] == "linux"

  file '/tmp/teste' do
    content 'is Linux'
  end

  template '/etc/resolv.conf' do
    source 'resolv.erb'
    owner 'root'
    group 'root'
    mode '0644'
    action :create
  end

  cookbook_file '/etc/ssh/sshd_config' do
    source 'sshd_config'
    owner 'root'
    group 'root'
    mode '0600'
    action :create
  end

  directory '/op/codeops/apps' do
    owner 'root'
    group 'root'
    mode '0755'
    recursive true
    action :create
  end

  user 'rootcodeops' do
    shell '/bin/bash'
    manage_home true
    home '/home/rootcodeops'
  end

  sudo 'admins' do
    user 'rootcodeops'
    group 'codeops'
    nopasswd true
  end


end
