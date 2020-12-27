# Flask Password Generator
A simple password generator built with Flask and built for testing DevOps processes.

# Requirements
- Flask*
- Docker 
- Jenkins

# Install
#### Flask
```
$ pip install -r requirements
```
#### Local
```
$ python app.py
```
#### Docker
```
$ docker run -d -p 80:80 dturan/flask-password-generator
```


#### Jenkins Plugins

To use Jenkinsfile, you need to install "Docker Pipeline" plugin on jenkins installed on your system.

| Plugin | README |
| ------ | ------ |
| Docker Pipeline | https://plugins.jenkins.io/docker-workflow/

# Using
```
localhost/generate/length
```

#### Examples
```
localhost/generate/12
```