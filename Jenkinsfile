pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                // build venv
                sh """
                #!/bin/bash
                pip3 install -r requirements.txt
                python3 getData.py
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