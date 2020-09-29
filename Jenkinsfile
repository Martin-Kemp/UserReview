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
            steps {
                // Perform tests eg: does file exist?
                sh """
                FILE=./userlist.html
                if [ -f "$FILE" ]; then
                    echo "$FILE exists."
                fi
                """

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