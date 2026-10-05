pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                // Replace with your actual student feedback repo URL if different
                git branch: 'main', url: 'https://github.com/Krish-Rajput/jenkins-demo-2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m pip install --upgrade pip
                    if exist requirements.txt (
                        pip install -r requirements.txt
                    )
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    python -m pytest
                '''
            }
        }

        stage('Build / Verify') {
            steps {
                echo 'Flask student feedback app verified successfully!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}