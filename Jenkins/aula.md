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


# Outros

1. rvm (permite instalar várias versões do ruby, divididos por versão ruby)

# Instalando RVM

```
  su - jenkins
  gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
  \curl -sSL https://get.rvm.io | bash -s stable
  echo "source /var/lib/jenkins/.rvm/scripts/rvm" ~/.bash_profile
```


## Gerar pacotes

1. [fpm](https://github.com/jordansissel/fpm)
2. bricklayer

### FPM
```
  yum install ruby-devel gcc make rpm-build rubygems rpm-build -y
  gem install fpm
```

# Usando

```
fpm -m "Kaio Cesar" --url "https://github.com/kaioaresi" --description "Teste enpacotamento" -a noarch -s dir -t rpm -n minha-api --rpm-user root --rpm-group root -v 0.1 --prefix /opt/app/minha-api .
```



# Teste de aplicações
> gem install sinatra

```
# app.rb

require 'sinatra'

get '/' do
  "Welcome"
end

get '/users' do
  "Usuers"
end
```

## Arquivo para realizar os testes

```
# tests.rb

require_relative 'app'
require 'test/unit'
require 'rack/test'

class MyTest < Test::Unit::TestCase
  include Rack::Test::Methods

  def app
    Sinatra::Application
  end

  def test_home_page
    get '/'
    assert last_response.ok?
    assert_equal 'Welcome', last_response.body
  end
end
```

fpm -m "Kaio Cesar" --url "https://github.com/kaioaresi" --description "App Sinatra" -a noarch -s dir -t deb -n app_sinatra --rpm-user root --rpm-group root -v 0.1 --prefix /opt/app/app_sinatra *.rb
