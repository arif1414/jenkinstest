pipeline {
    agent any

    stages {
        stage('env') {
            steps {
                sh '''#!/bin/bash -l
                echo 'he he'
                env
                echo "=====here=========="
                echo $GIT_COMMIT
                git diff-tree -r $GIT_COMMIT --no-commit-id --name-only
                ls -lrt
                which python
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
