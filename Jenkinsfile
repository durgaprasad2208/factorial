pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/durgaprasad2208/factorial.git'
            }
        }

        stage('Run Python Code') {
            steps {
                bat 'python factorial.py'
            }
        }
    }
}