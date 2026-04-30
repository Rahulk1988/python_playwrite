pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat 'python -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -v --html=reportplay.html'
            }
        }
    }
}