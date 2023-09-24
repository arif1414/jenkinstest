pipeline {
    agent any

    stages {
        stage('Master Branch Tasks') {
            when {
                branch 'master'
            }
            steps {
              sh '''#!/bin/bash -l
              echo 'main branch'
              '''
            }
        }
        stage('Example (Not master)') {
           when {
               not {
                   branch 'master'
               }
           }
           steps {
              sh '''#!/bin/bash -l
              echo 'other branch'
              '''
           }
        }
    }
}
