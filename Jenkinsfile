pipeline {
    agent any

    stages {
        stage('env') {
            steps {
                sh '''#!/bin/bash -l
                echo 'he he'
                env
                '''
            }
        }
        stage('Master Branch Tasks') {
            //when {
            //        environment(name: "GIT_BRANCH", value: "origin/main")
            //    }
              when {
                expression {env.GIT_BRANCH == 'origin/main'}
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
                expression {env.GIT_BRANCH != 'origin/main'}
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
