pipeline {
    agent any

    stages {
        stage('Master Branch Tasks') {
            when {
                    {
                        environment(name: "deployBranch", value: "main")
                    }
                }
                steps {

                        <anything goes here like groovy code or shell commands>
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
