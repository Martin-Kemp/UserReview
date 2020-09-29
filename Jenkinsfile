pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                // build venv
                sh """
                #!/bin/bash
                python3 getData.py
                """
            }
        }
        stage('Test') { 
                // Perform tests eg: does file exist?
                def exists = fileExists './userlist.html'
                if (exists) {
                    echo 'Yes'
                } else {
                    echo 'No'
                }
        }
        stage('Deploy') { 
            steps {
                // Start server
                sh 'cp ./userlist.html /var/www/html/index.html'
            }
        }
    }
}