pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout source code from GitHub repository
                git branch: 'main', url: 'https://github.com/Jaisuryan-web/GITHUB_ACTIONS-.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                    "C:\\Python311\\python.exe" -m venv venv
                    call venv\\Scripts\\activate.bat
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies & Run') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    if exist requirements.txt pip install -r requirements.txt
                    python --version
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
    }
}
