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


#
