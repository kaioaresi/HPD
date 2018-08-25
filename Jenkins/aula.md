# É uma ferramenta de automatização
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
