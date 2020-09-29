pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                // build venv
                sh 'python3 -m venv venv'
                sh 'source ./venv/bin/activate'
                sh 'pip install -r requirements.txt'
                // get data
                sh 'python getData.py'
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