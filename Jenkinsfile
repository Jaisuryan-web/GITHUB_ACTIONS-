pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Jaisuryan-web/GITHUB_ACTIONS-.git'
            }
        }

        stage('Setup & Install Dependencies') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest
                '''
            }
        }

        stage('Run Billing App') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    python billing.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    pytest test_billing.py
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
