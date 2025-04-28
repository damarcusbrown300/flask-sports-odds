pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "damarcusbrown/flask-sports-odds"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/damarcusbrown300/flask-sports-odds.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker stop flask-sports-odds || true'
                    sh 'docker rm flask-sports-odds || true'
                    sh "docker run -d -p 8080:8080 --name flask-sports-odds ${DOCKER_IMAGE}"
                }
            }
        }
    }
}
