pipeline {
    agent any

    stages {
        stage('build environment') {
            steps {
              //withPythonEnv("/usr/bin/python3") {
              //  script {
                  sh '''#!/bin/bash -l
                  env
                  '''
                  //sh "pip install -r requirements.txt"
              //  }
              //}
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
