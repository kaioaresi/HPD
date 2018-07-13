# Definindo image base do OS
FROM centos:7

# Quem mantem a imagem
MAINTAINER aresi [kaioaresi@gmail.com]

# Realizando procedimento de instalação
# Observação sempre limpe a casa
RUN yum install epel-release -y ; yum install nginx -y ; yum clean all

# Copiando index personalizado
COPY index.html /usr/share/nginx/html/

# Definindo processo que será mantido em execução
ENTRYPOINT ["/usr/sbin/nginx", "-g","daemon off;"]

# Definindo porta que será utilizada
EXPOSE 80
