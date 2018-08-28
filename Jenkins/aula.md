# É uma ferramenta de orguestração
> https://jenkins.io/

## Instalando jenkins

```
yum install java-1.8.0 -y
wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
yum install jenkins dejavu-sans-fonts fontconfig git bash-completion -y
```

## Iniciando o jenkins
```
/etc/init.d/jenkins start
# logs
tailf /var/log/jenkins/jenkins.logs
# acesse a url
http://<servidor>:8080
  cat /var/lib/jenkins/secrets/initialAdminPassword
```

## jenkins executado docker

```
  # instale o docker
    curl -fsSl https://get.docker.com | bash
  # habilitando bash do jenkins
    usermod -s /bin/bash jenkins
    usermod -aG docker jenkins
    systemctl restart jenkins
```

## Plugins
> https://plugins.jenkins.io/

1. Blue ocean
2. Dashboards
3. Build Monitor view
4. Monitoring


## Themas

1. http://afonsof.com/jenkins-material-theme/
2. https://tobix.github.io/jenkins-neo2-theme/
3. https://github.com/rackerlabs/canon-jenkins


# Performance
> https://jenkins.io/blog/2016/11/21/gc-tuning/
