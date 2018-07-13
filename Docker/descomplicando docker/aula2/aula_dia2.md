# Trabalhando com volumes

> NUNCA GUARDAR NENHUM DADOS DENTRO DOS CONTAINERS

O docker trabalha com dois tipos de volumes bind e volume.

1. Bind é usado quando um diretorio já existe e você não pode alterar o mesmo.

2. Volume utilizado quando você pode criar uma novo volume para utilizar na aplicação.

3. Agora vamos criar um diretorio de volumes (forma antiga)

```bash
  mkdir /volumes
```

Vamos subir um container com apontando para um volume

```docker
  docker container run -ti -v <meu volume local>:<meu volume do container> <outros>
  docker container run -ti -v /vomules:/teste_volume ubuntu
```
Agora dentro do container crie um arquivo teste e saia do container, acesar o diretorio local do `volumes` o arquivo estará lá.

3.1 Trabalhando volumes do tipo `volume` quando o volume for criado pelo `docker volume`.

```docker
  docker volume create meu_volume
  docker volume  inspect meu_volume # para saber onde seu volume está sendo salvo
  docker container run -ti --mount type=volume,src=meu_volume_teste,dst=/volume_teste ubuntu
```

Quando você criar um arquivo no diretorio local ou no arquivo, o mesmo será compartilhando entre o container e o diretorio local.

3.2 Trabalhando com volume tipo `bind`.

Para ser utilizado quando o volume for um diretorio existente no host, e não for criado pelo `docker volume`, deve se passar o caminho do diretorio completo.

```docker
  docker container run -ti --mount type=bind,src=/volumes,dst=/meu_volume ubuntu
```


**Dica:**
É possível passar um comando para ser executando dentro do container que será exido fora do mesmo, exemplo:

Aqui vamos subir um container ubuntu e quando esse container subir ele vai executar um comando detro dele e a saída será exibida na tela;

```docker
  docker container run -ti ubuntu ls -lh /tmp
```
> Neim todos container pode-ser fazer isso, lembrese que existe apenas um processo que roda em front, no caso o ubuntu é o bash, por isso é possível realizar o exemplo acima.


## Como subir um hub particular
Existem uma solução chamada `registry` que possibilitar subir um container com hub particular

```docker
  docker container run -d -p 5000:5000 registry:2
```

Como fazer o upload de image para o `registry` local

```docker
  docker tag <id image> localhost:5000/nginx_ssl:1.1
```






















#
