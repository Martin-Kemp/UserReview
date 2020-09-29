pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                // build venv
                sh """
                #!/bin/bash
                pip install -r requirements.txt
                python getData.py
                """
            }
        }
        stage('Test') { 
            steps {
                // Perform tests eg: does file exist?
                sh 'ls -la'
            }
        }
        stage('Deploy') { 
            steps {
                // Start server
                sh 'echo test'
            }
        }
    }
}