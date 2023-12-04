pipeline {
  agent any
  environment {
    registry = 'dturan/flask-password-generator:latest'
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  stages {
    stage('Git'){
        steps{
            git credentialsId: 'github', url: 'https://github.com/dogukanturan/flask-password-generator'
        }
    }
    stage('Building Image') {
      steps{
        script {
          dockerImage = docker.build registry
        }
      }
    }
    stage('Deploy Image') {
        steps {
            script {
                docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                }
            }
        }
    }
    stage('Clean Unused Image') {
      steps{
        sh 'docker rmi $registry'
      }
    }
  }
}
