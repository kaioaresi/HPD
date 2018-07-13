FROM ubuntu
MAINTAINER aresi [aresikaio@gmail.com]
RUN apt-get update && apt-get install nginx -y && apt-get clean
COPY index.html /var/www/html/
ENTRYPOINT ["/usr/sbin/nginx", "-g","daemon off;"]
EXPOSE 80
