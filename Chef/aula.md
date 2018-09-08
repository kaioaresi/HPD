# Aula 1


## O que é o [Chef](https://www.chef.io/chef/) ?

  Chef é um gerenciado de configuração, que utiliza um cliente.

Componentes
  - Chef manager;
  - Chef cliente
  - Workstation (para os adms)
## O que é um cmdb ?
  É uma software para controlar inventario do ambiente.

---

# Rodando chef solo
> https://downloads.chef.io/

## Instalando Chef Development Kit

```
  wget https://packages.chef.io/files/stable/chefdk/3.1.0/el/7/chefdk-3.1.0-1.el7.x86_64.rpm
  rpm -ivh chefdk-3.1.0-1.el7.x86_64.rpm
  chef # para testar
```
## Criando receitas
> Obs: Os arquivos devem ter extencion `rb`

**receita.rb**
```
file '/tmp/motd' do
  content 'Cuidado ao logar neste host, estamos monitorando!'
end
```
#### Executando uma receita

```
  chef-client <minha receita>.rb
  chef-client --local-mode <minha receita>.rb # para rodar local
```


[`Actions`](https://docs.chef.io/resource_execute.html): são funções já prontas do chef que te permite realizar algumas tarefas.
Docs recursos https://docs.chef.io/resource_reference.html


#### Pegando informação do node
```
puts node['platform']
```

#### Criando Conficionais

```
if node['platform'] == "ubuntu"
  file '/tmp/ubuntu-server' do
    content 'servidor ubuntu'
    action :create
  end
end
```

#### Instalando pacote

```
  package '<nome do pacote>'
# or
  package '<nome do pacote>' do
    allow_downgrade            True, False
    arch                       String, Array
    flush_cache                Array
    notifies                   # see description
    options                    String
    package_name               String, Array # defaults to 'name' if not specified
    source                     String
    subscribes                 # see description
    timeout                    String, Integer
    version                    String, Array
    action                     Symbol # defaults to :install if not specified
  end
```

#### Criando usuário

```
user '<nome do usuario>' do
  comment                    String
  force                      True, False # see description
  gid                        String, Integer
  home                       String
  iterations                 Integer
  manage_home                True, False
  non_unique                 True, False
  notifies                   # see description
  password                   String
  salt                       String
  shell                      String
  subscribes                 # see description
  system                     True, False
  uid                        String, Integer
  username                   String # defaults to 'name' if not specified
  action                     Symbol # defaults to :create if not specified
end

# exemple

user 'teste' do
  comment 'A random user'
  uid '1234'
  gid '1234'
  home '/home/random'
  shell '/bin/bash'
  password '$1$JJsvHslasdfjVEroftprNn4JHtDi'
end

# outra opção simples
user 'kaio' do
        manage_home true
        home '/home/kaio'
        shell '/bin/bash'
end
```

#### Serviços

```
service '<nome do serviço>' do
  action [:<opção 1>, :<opção 2>]
end

# exemplo

service 'nginx' do
  action [:start, :enable]
end

```

---

# Padrões no chef

#### Forma manual
1. Crie um diretorio `chef-repo` no diretorio de sua preferencia
2. Já dentro do dir `chef-repo`, crie um novo dir `cookbooks` mova suas receita para dentro deste diretorio

#### Forma automatica
1. Criando estrutura repositorio chef

```
  chef generate repo <nome do diretorio>
# exemplo
  chef generate repo chef-repo
```

#### Criando dir cookbooks
```
  chef generate cookbook cookbooks/<meu projeto>
# exemplo
  chef generate cookbook cookbooks/meu_servidor_web

```

#### Executando cookbook

```
  chef-client --local-mode --runlist 'recipe[<nome cookbook>::<nome arquivos dentro do recipe>]'
  chef-client -z --runlist 'recipe[meu_servidor_web::nginx]'
```

#### Gerando `recipes`

```
  chef generate recipe cookbooks/<meu cookbook> <nome receita>

# exemplo

  chef generate recipe cookbooks/elastic elastic
```
#### Criando file

```
  chef generate file cookbook/elastic motd
```

##### Entregrado arquivo estatico

```
cookbook_file '/var/www/customers/public_html/index.php' do
  source 'index.php'
  owner 'web_admin'
  group 'web_admin'
  mode '0755'
  action :create
end
# exemplo

cookbook_file '/etc/motd' do
  source 'motd'
  owner 'root'
  group 'root'
  mode '0644  '
  action :create
end
```


#### Entregando arquivo dinamicamente com dados de acordo com o host (template)

> Todo arquivo de template dem que ter a extenção `.erb`

```
  chef generate template cookbooks/<projeto name> <file name>
  chef generate template cookbooks/elastic motd.erb
```

###### Conteudo do arquivo

```
# Arquivos gerenciado pelo Chef
<% if node['platform'] == "centos" %>
Ola, você está sendo monitorando seu host é um Centos
<% end %>
```

```
template '/etc/motd' do
  source 'motd.erb'
  owner 'root'
  group 'root'
  mode '0644  '
  action :create
end
```

### Atributs
É um arquivo onde é declarado todas variavel que serão utilizadas no template


```
  chef generate attribute cookbooks/<meu cookbook> <nome arquivo attribute>
# exemple
  chef generate attribute cookbooks/elastic padrao

```


#### Escrevento arquivo attribute

##### Declarando variavel attribute

```
node.default['item1'] = 'Centos'
node.default['item2'] = 'Debian'
```

##### No arquivo o Arquivo

```
<% if node['platform'] == "centos" %>
  Ola, Seja bem vindo !!! você está utilizando um <%= node['item1'] %>
<% else %>
  Ola, Seja bem vindo !!! você está utilizando um <%= node['item2'] %>
<% end %>
```

## Execute para executar scripts

```
execute 'apache_configtest' do
  command '/usr/sbin/apachectl configtest'
end
```

# Parte 2: Chef server

>https://downloads.chef.io/chef-server/12.17.33

#### Centos
```
    wget https://packages.chef.io/files/stable/chef-server/12.17.33/el/7/chef-server-core-12.17.33-1.el7.x86_64.rpm

    rpm -ivh chef-server-core-12.17.33-1.el7.x86_64.rpm

```

##### Configurando o chef automaticamente

```
  chef-server-ctl reconfigure
```

### Personalizando as configurações do chef-server

```
  vim /etc/opscode/chef-server.rb
# modelo de configuração
  # variavel
  server_name = '192.168.1.6'

  api_fqdn = server_name
  bookshelf['vip'] = server_name
  nginx['url'] = "https://#{server_name}"
  nginx['server_name'] = server_name
  lb['fqdn'] = server_name

# Agora é reconfigure
  chef-server-ctl reconfigure
```


###### Verificando serviços iniciado pelo chef

```
  chef-server-ctl status
```

##### Chef Organization

> Tips: O chef server usa a porta 80, por padrao
> Tips: Logs `/var/log/opscode/nginx/current`

Criando um Organization

```
  chef-server-ctl org-create <sort name> <full name>  -f ""<diretorio>/<key>.pem"
# exemplo
  chef-server-ctl org-create aresi "Aresi corp." -f aresi.pem
```

Deletando um Organization

```
  chef-server-ctl org-delete <sort name>
# exemplo
  chef-server-ctl org-delete teste
```

Criando usuário

```
  chef-server-ctl user-create USERNAME FIRST_NAME [MIDDLE_NAME] LAST_NAME EMAIL PASSWORD -f <keu>.pem

# Exemplo

  chef-server-ctl user-create kaioaresi Kaio Fernandes Santos kaioaresi@teste.com '123456' -f <keu>.pem

```

Add usuário a Organization

> O primeiro usuário se torna o admin da Organization

```
  chef-server-ctl org-user-add ORG_NAME USER_NAME
# Exemplo
  chef-server-ctl org-user-add aresi kaioaresi

```

Tornar outros usuário admin
```
  chef-server-ctl org-user-add ORG_NAME USER_NAME --admin
# Exemplo
  chef-server-ctl org-user-add aresi kaioaresi --admin

```

---

# Instalando knife

É um cliente para permitir que o admin desenvolva cookbooks para o chef, que depois é enviado para ser executando no chef-server.

```

  wget https://packages.chef.io/files/stable/chefdk/3.1.0/el/7/chefdk-3.1.0-1.el7.x86_64.rpm
  rpm -ivh chefdk-3.1.0-1.el7.x86_64.rpm

```

---

## Configurando knife

Conectando ao chef-server
> Apenas um knife por organization

```
  knife configure

    # informações importantes
    https://<ip chef-server>/organization/<nome organization>
    https://192.168.1.6/organizations/aresi
```

Agora vamos colocar a chave em nosso host development knife, para dentro o diretorio no host de desenvolvimento.

> Tips: Lembre-se de ter criado o usuário no chef-server

```
  <home user>/.chef/<user>.pem
```

Testando a conexão e corrigindo o erro

```
  # Execute um comando qualquer para testar a conexão, irá ocorrer um erro então será necessário baixar o certificado
  knife user list

  # Para baixar o certificado e execute o comando novamente
  knife ssl fetch

  knife user list

```

---

# Time to work!

Agora vamos criar nossos cookbooks

#### Criando repositorio e um cookbook para enviar o chef-server

```
    chef generate repo <nome do repo>
    chef generate cookbook cookbooks/<projeto>
    cd cookbooks/<projeto>
      package 'nginx'
      service 'nginx' do
        action [:enable, :start]
      end      
```

Configurando o path dos cookbooks no knife

```
cookbook_path = ['<dir full>/cookbooks']
```

Enviado cookbook para chef-server

```
  knife cookbook upload <nome do cookbook> -o <path cookbook> # caso não funcione
  knife cookbook list
```

---

#### Add node com knife no chef-server

```
  knife bootstrap <ip> -N <nome do host|hostname> -x <user> -p <port> -P <password>|-i <certificado> --sudo

# Exemplo

  knife bootstrap 192.168.1.6 -N chef_manager_teste -x root -p 22 -P '123'
  knife bootstrap node list
  knife bootstrap node show <nome do node>
```

Agora vamos executar uma receita no node remoto
```
  knife ssh 'name:<nodename|*>' "chef-client -r 'recipe[nome receita|cookbook]'" -x root -p 22890 -P '<password>' -a ipaddress

  # Obs: O menos `-a` é para ele conectar usando o ip e não o hostname

  knife ssh 'name:lab_chef_client' "chef-client -r 'recipe[treino1]'" -x root -p 22890 -P '123' -a ipaddress
```


#### Criando enviriment

```
  export EDITOR=vim
  knife environment create
  # Recriando o node add environment e runlist em perguntar
  knife bootstrap 192.168.1.11 -N cobaia_chef_client -x root -p 22 -P '123' -E prod -r 'recipe[treino1]' -y
```












#
