pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r application\\requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t devops-flask-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop devops-flask-container || exit 0'
                bat 'docker rm devops-flask-container || exit 0'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 8080:5000 --name devops-flask-container devops-flask-app'
            }
        }
    }

    post {

        success {
            echo '======================================'
            echo 'CI/CD PIPELINE SUCCESSFUL!'
            echo 'Application is running on port 8080'
            echo '======================================'
        }

        failure {
            echo '======================================'
            echo 'CI/CD PIPELINE FAILED!'
            echo 'Check the Console Output'
            echo '======================================'
        }
    }
}