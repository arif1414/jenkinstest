pipeline {
    agent any

    stages {
        stage('env') {
            steps {
                sh '''#!/bin/bash -l
                env
                pwd
                ls -lrt
                '''
            }
        }
        stage('Command Plan') {
            steps {
              sh '''#!/bin/bash -l
              echo "Git Branch $GIT_BRANCH"
              ./buildcommands.sh
              '''
            }
        }
        stage('Command execution') {
            when {
                expression {env.GIT_BRANCH == 'origin/main'}
            }
            steps {
              sh '''#!/bin/bash -l
              echo "Git Branch $GIT_BRANCH"
              ./executecommands.sh
              '''
            }
        }
    }
}