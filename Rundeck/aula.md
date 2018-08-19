# Rundeck

É um orguestrador de comandos, que permite a centralizador de execuções (#crontab,#agendador).

## Instalação

```
yum install java-1.8.0 -y
rpm -Uvh http://repo.rundeck.org/latest.rpm
yum install rundeck -y
systemctl start rundeckd
# porta 4440
# user/pass: admin
```

## Configurando rundeck

```
  vim /etc/rundeck/framework.properties
    framework.server.name = <ip do servidor | dns>
    framework.server.hostname = <ip do servidor | dns>
    framework.server.port = 4440
    framework.server.url = http://<ip do servidor | dns>:4440

  vim /etc/rundeck/rundeck-config.properties
    grails.serverURL=http://<ip do servidor | dns>:4440
```

## Declarando node remoto

  etc/resource.yml
```
ntb.local:
  hostname: 192.168.1.5
  nodename: ntb
  osArch: x86_64
  username: rundeck  
```

## Configurando o node (client)

Ainda no servidor rundeck copie a chava publica.
```
    su - rundeck
    cat .ssh/id_rsa.pub    
```

No node

```
  adduser rundeck
  su - rundeck
  mkdir .ssh
  vim .ssh/authorized_keys
  chown rundeck. .ssh; -R
```


# Trabalhando com api do rundeck

Trabalhar com apis proporciona a integração e automatização de ferramentas é muito importante saber trabalhar com apis.
> https://rundeck.org/docs/api/

1. Gerar token para autenticação da api;
2. Testando token com uma chamada simples;
### GET
```
  curl -XGET -H 'X-Rundeck-Auth-Token: <token>' -H 'Accept: application/json' <endereço rundeck>/api/<version>/rota
  curl -XGET -H 'X-Rundeck-Auth-Token: fgXzCKbwO4fpGglosRjZFa6B1h9N2wjC' -H 'Accept: application/json' http://192.168.1.4:4440/api/19/system/info
```

### Post

```
  curl -XPOST -H 'X-Rundeck-Auth-Token: <token>' -H 'Accept: application/json' <endereço rundeck>/api/<version>/
  curl -XPOST -H 'X-Rundeck-Auth-Token: fgXzCKbwO4fpGglosRjZFa6B1h9N2wjC' -H 'Accept: application/json' -d '{"argString":"-usuario kaio -ambiente hml"}' http://192.168.1.4:4440/api/25/job/eca6e5c8-0168-4620-9ad3-4ba1d5cd809c/run

  curl -XPOST -H 'X-Rundeck-Auth-Token: fgXzCKbwO4fpGglosRjZFa6B1h9N2wjC' -H 'Accept: application/json'  http://192.168.1.4:4440/api/25/job/eca6e5c8-0168-4620-9ad3-4ba1d5cd809c/run
    {
      "argString":"...",
      "loglevel":"...",
      "asUser":"...",
      "filter":"...",
      "runAtTime":"...",
      "options": {
          "usuario":"kaio",
          "ambiente":"hml",
      }
    }

```

## Secret keys

Configurações >> key storage >> Add or Upload a Key >> crie uma nova senha


## ACL

Todo arquivo de acl deve ter o a extenção `.aclpolicy`.
exemplos:

```
description: Permissões de jr
context:
  project: Projeto_1
for:
  resource:
    - equal:
      kind: job
      allow: [running, read]
by:
  group: junior


```


---
