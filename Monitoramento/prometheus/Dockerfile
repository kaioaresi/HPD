FROM prom/prometheus:v2.3.1
MAINTAINER kaioaresi [https://github.com/kaioaresi]

RUN mkdir /etc/prometheus/rules
COPY prometheus.yml /etc/prometheus/
COPY rules/ /etc/prometheus/rules/
