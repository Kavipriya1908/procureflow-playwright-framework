pipeline {
    agent any

    environment {
        BASE_URL       = 'https://sellus.us'
        API_BASE_URL   = 'https://api.sellus.us'
        VALID_EMAIL    = credentials('procureflow-email')
        VALID_PASSWORD = credentials('procureflow-password')
    }

    stages {
        stage('Install') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\pip install -r requirements.txt'
                bat '.venv\\Scripts\\python -m playwright install chromium'
            }
        }
        stage('Smoke Tests') {
            steps {
                bat '.venv\\Scripts\\python -m pytest -m smoke'
            }
        }
    }

    post {
        always {
            allure results: [[path: 'reports/allure-results']]
        }
    }
}
