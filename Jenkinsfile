pipeline {
    agent any

    stages {
        stage('env') {
            sh '''#!/bin/bash -l
            echo 'he he'
            env
            '''
        }
        stage('Master Branch Tasks') {
            when {
                    environment(name: "deployBranch", value: "main")
                }
            steps {
              sh '''#!/bin/bash -l
              echo 'main branch'
              cat ./Jenkinsfile
              '''
            }
        }
        stage('Example (Not master)') {
           when {
               not {
                   branch 'main'
               }
           }
           steps {
              sh '''#!/bin/bash -l
              echo 'other branch'
              cat ./Jenkinsfile
              '''
           }
        }
    }
}
