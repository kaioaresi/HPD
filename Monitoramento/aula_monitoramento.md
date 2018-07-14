# Monitoramento


## Netdata
1. instalando [netdata](https://github.com/firehol/netdata);
```
  bash <(curl -Ss https://my-netdata.io/kickstart.sh)
```
2. Configurando registry

```bash
  cd /etc/netdata/netdata.conf
  # Busque a palavra "[registry]" e descomente os seguintes campos, essa conf é para o manager
    enabled = yes
    registry to announce = http://<seu ip>:19999
    reegistry hostname = <nome do host>
    systemctl restart netdata
```

```bash
  # configurando os nodes
  enabled = no
  registry to announce = http://<ip do manager>:19999
  reegistry hostname = <nome do host>
  systemctl restart netdata
```

## Prometheus
> Criar uma imagem prometheus com porta alta

1. Baixnando [Prometheus](https://github.com/prometheus/prometheus/releases/download/v2.3.1/prometheus-2.3.1.linux-amd64.tar.gz)
```
  curl -LO https://github.com/prometheus/prometheus/releases/download/v2.3.1/prometheus-2.3.1.linux-amd64.tar.gz
  tar -zxvf prometheus-2.3.1.linux-amd64.tar.gz
  cd prometheus-2.3.1.linux-amd64
  cp prometheus /usr/local/bin/
  cp promtool /usr/local/bin/
  adduser --no-create-home --shell /bin/false prometheus
  adduser --no-create-home --shell /bin/false node_exporter
  chown prometheus. /usr/local/bin/prometheus
  chown prometheus. /usr/local/bin/promtool
  mkdir /etc/prometheus
```

























#
