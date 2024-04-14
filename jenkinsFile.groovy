pipeline {
    agent any
    stages {
        stage('Build'){
            sh 'pip install -r requirements.txt'
        }
        stage('Tests'){
            sh 'python -m pytest '
        }
        stage('Check windows service status'){
            sh 'pwsh check_services.ps1' 
        }
    }
}