# Stacks

- ELK - elasticsearch + logstash + kibana
- elastic + beats + kibana

# Instalando componentes

1. Java 1.x

```
  yum install java-1.8.0-openjdk  
```

2. elasticsearch

```
  yum install https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.3.1.rpm
```

3. Kibana

```
  yum install -y https://artifacts.elastic.co/downloads/kibana/kibana-6.3.1-x86_64.rpm
```

# Configurando stak

1. Elasticsearch

```
  vim /etc/elasticsearch/elasticsearch.yml

    network.host: <seu ip atual>

  # Teste
    curl http://192.168.1.7:9200
```

2. Kibana
```
  vim /etc/kibana/kibana.yml
    server.host: <ip publico>
    elasticsearch.url: <ip do elasticsearch>

```

3. Instalando e configurando packetbeat (client)

> https://www.elastic.co/products/beats/packetbeat
> https://artifacts.elastic.co/downloads/beats/packetbeat/packetbeat-6.3.2-x86_64.rpm
```
  wget "https://artifacts.elastic.co/downloads/beats/packetbeat/packetbeat-6.3.2-x86_64.rpm"
  rpm -ivh packetbeat-6.3.2-x86_64.rpm
  cd /etc/packetbeat
  vim packetbeat.yml
    # elasticsearch
    hosts: ["<ip elasticsearch>:9200"]
    # kibana
    hosts: ["<ip kibana>:5601"]
    # dashboards
    setup.dashboards.enabled: true

  # start
  /etc/init.d/packetbeat start
```

4. Filebeat

> https://www.elastic.co/products/beats/filebeat

```
  wget "https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.3.2-amd64.deb"
  dpkg -i filebeat-6.3.2-amd64.deb
  vim /etc/filebeat/filebeat.yml
      # inputs
      enabled: true
      # elasticsearch
      hosts: ["<ip elasticsearch>:9200"]
      # kibana
      hosts: ["<ip kibana>:5601"]
      # dashboards
      setup.dashboards.enabled: true
```
# Configurando modulo nginx

## Host elasticsearch manager, configurar

```
  cd /usr/share/elasticsearch/bin/
    ./elasticsearch-plugin install ingest-user-agent
    ./elasticsearch-plugin install ingest-geoip
    /etc/init.d/elasticsearch restart
```



## Host client filebeat
> https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-nginx.html

```
  # listar moduloes disponiveis
  filebeat modules list
  filebeat modules enable nginx
  cd /etc/filebeat/modules.d
  vim nginx.yml
    - module: nginx
      # Access logs
      access:
      enabled: true

      # Set custom paths for the log files. If left empty,
      # Filebeat will choose the paths depending on your OS.
      var.paths: ['/var/log/nginx/access.log']

      # Error logs
      error:
      enabled: true

      # Set custom paths for the log files. If left empty,
      # Filebeat will choose the paths depending on your OS.
      var.paths: ['/var/log/nginx/error.log']

```

## Host metric beats

> https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-6.3.2-amd64.deb

```
  vim /etc/metricbeat/metricbeat.yml
    # inputs
    enabled: true
    # elasticsearch
    hosts: ["<ip elasticsearch>:9200"]
    # kibana
    hosts: ["<ip kibana>:5601"]
    # dashboards
    setup.dashboards.enabled: true

```

## Habilitando modulo do docker

```
  sudo metricbeat modules enable docker
  sudo /etc/init.d/metricbeat restart
```

## Host heartbeat

> https://artifacts.elastic.co/downloads/beats/heartbeat/heartbeat-6.3.2-amd64.deb

```
  vim /etc/heartbeat/heartbeat.yml
    # Heartbeat
      urls: [''] # url para monitorar
    # elasticsearch
    hosts: ["<ip elasticsearch>:9200"]
    # kibana
    hosts: ["<ip kibana>:5601"]
    # dashboards
    setup.dashboards.enabled: true

```


# Beats windows
> https://artifacts.elastic.co/downloads/beats/winlogbeat/winlogbeat-6.3.2-windows-x86_64.zip

```
  # donwload do pacote

```
