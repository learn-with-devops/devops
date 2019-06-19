pipeline {
    agent any
    stages {
        stage('Preparation') {
            steps {
                      sh 'mvn archetype:generate -B ' +
                    '-DarchetypeGroupId=org.apache.maven.archetypes ' +
                    '-DarchetypeArtifactId=maven-archetype-quickstart ' +
                    '-DgroupId=com.company -DartifactId=myproject'
            }
        }
    stage('Build') {
           steps {
            dir ('myproject') {
                 
                sh 'mvn clean install test'
            }   
        } 
       
   }
   stage('Archive') {
         steps {
           dir ('myproject/target') {
           archive '*.jar'
         }  
      } 
      
   }  
    }
    post {
        always {
            echo 'I have finished and deleting workspace'
            deleteDir() 
        }
        success {
            echo 'Job succeeeded!'
        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'I failed :('
        }
        changed {
            echo 'Things were different before...'
        }
    }
}
