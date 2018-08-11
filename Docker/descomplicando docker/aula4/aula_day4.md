
# Secret

Permite armazenar senha|certificados e gerando um hash do mesmo

1. Criando um docker secret com saida e file

```
echo "123123" | docker secret create minha_senha -
docker secret create minha_senha_file arquivo.txt
# Dentro do arquivo tem que ter a senha
```
> o sinal de  `-` diz que a key é partindo de uma sdtout


2.  Como usar a secret

```
  docker service create --name teste1 -p 8080:80 --secret source=<nome da secret>,target=<nome do arquivo da secret> kaioaresi/nginx_centos7:1.0
```

3. Alterando uma secret
```
  docker service update --secret-rm <secret para remover> --detach=false --secret-add source=<secret nova>,target=<nome file secret dentro do contianer>,mode=0400 <imagem>
```

---

# Compose

1. Instalando compose

```
curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose ; chmod +x /usr/local/bin/docker-compose
```
2. Criando um compose

```
version: '3.1'
service:
  # nome do serviço
  servidor_web:
      image: kaioaresi/nginx_centos7:1.0
      deploy:
          replicas: 2
          resources:
              cpus: "0.1"
              memory: 50m
          restart_policy:
              condition: on-failure
      ports:
        - "80:80"
      networks:
        - webservice
networks:
  webservice:

```
3. Fazendo update de serviço se o serviço cair

Existem duas opções
3.1. Não remover a stack e executar novamente a mesma linha para subir a stack, logicamente o arquivo deve ser alterado primeiro e depois a linha para subir a stack deve ser executada, os containers serão atualizados aos poucos.
```
  docker stack deploy -c docker-compose.yml <mesmo nome do serviço>
```

```
version: '3.6'
service:
  servidor_web:
    image: nginx
    deploy:
      mode: global
      restart_policy: on-failure
    ports:
      - 80:80
```
3.2














































#
