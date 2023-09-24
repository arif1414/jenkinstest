pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                git branch: 'main', credentialsId: 'arifgithub', url: 'https://github.com/arif1414/jenkinstest'
            }
        }
    }
}
