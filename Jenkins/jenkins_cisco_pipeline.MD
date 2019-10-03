## Jenkins Pipeline


    def branch

    def getDeploymentEnvironment() {
        if (env.BRANCH_NAME.startsWith('PR-')) {
            return 'PR'
        } else {
            return env.BRANCH_NAME
        }   
    }

    pipeline {
    agent any
    stages {
        stage('Directory Assignment') {
            steps {
                script{

                    branch = "${getDeploymentEnvironment()}"
                    echo "the present branch is: ${branch}"

                    sh 'python git_dir.py'
                    sh 'pwd'

                    env.WORKSPACE = pwd()

                    def fh2 = readFile "${env.WORKSPACE}/folder_list.txt"
                    //File fh2 = readFile('./folder_list.txt')
                    def lines = fh2.readLines()
                    for (line in lines) {
                        folder = line
                    }
                    dd = lines.findAll { it.contains('cmp/collectors/emc-data-domain') }
                    emcdatafolder = dd.toString()

                    vnx = lines.findAll { it.contains('cmp/collectors/emc-vnx') }
                    emcvnxfolder = vnx.toString()

                    ucsb = lines.findAll { it.contains('cmp/collectors/ucs-bseries') }
                    ucsbseriesfolder = ucsb.toString()

                    ucsc = lines.findAll { it.contains('cmp/collectors/ucs-cseries') }
                    ucscseriesfolder = ucsc.toString()

                    ucsfi= lines.findAll { it.contains('cmp/collectors/ucs-fi') }
                    ucsfifolder = ucsfi.toString()

                    telegraf = lines.findAll { it.contains('cmp/collectors/telegraf') }
                    telegraffolder = telegraf.toString()

                    grafanadb = lines.findAll { it.contains('cmp/visualization/grafana_dashboards') }
                    grafanadashboardsfolder = grafanadb.toString()

             }
                }
            }

        stage('Test') {
                steps {
                    script {
                            echo "All test checks will run from here"
                    }

                }
            }

        stage('PR Deployment') {

                when {
                    expression { branch == 'PR' }
                }

                steps {
                    script {
          sh 'echo test >> folder_list.txt'
          sh 'cat folder_list.txt'
                            echo "Only Test Cases are runnig..."

                    }
                }
            }    


        stage('Build emc-data-domain') {
            when {
        allOf{
          expression { emcdatafolder == '[cmp/collectors/emc-data-domain]' }
          expression { branch != 'PR' }
        }
            }
            steps {
          script { 
                                 echo 'Building and Uploading the emc-data-domain docker image'
                                 sh 'chmod 755 cmp/collectors/emc-data-domain/build.sh'
                                 sh './cmp/collectors/emc-data-domain/build.sh'
                       }
                  }
      }


        stage('Build emc-vnx') {
            when {
                expression { emcvnxfolder == '[cmp/collectors/emc-vnx]' }
            }
            steps {
                script { 
                echo 'Building and Uploading the vnx docker image'
                sh 'chmod 755 cmp/collectors/emc-vnx/build.sh'
                            sh './cmp/collectors/emc-vnx/build.sh'
                    }
                }
            } 

        stage('Build ucs-bseries') {
            when {
                expression { ucsbseriesfolder == '[cmp/collectors/ucs-bseries]' }
            }
            steps {
                script { 
                        echo 'Building and Uploading the ucs-bseries docker image'
              sh 'chmod 755 cmp/collectors/ucs-bseries/build.sh'
                        sh './cmp/collectors/ucs-bseries/build.sh'

                    }
                }
            }

        stage('Build ucs-cseries') {
            when {
                expression { ucscseriesfolder == '[cmp/collectors/ucs-cseries]' }
            }
            steps {
                script { 
                        echo 'Building and Uploading the ucs-cseries docker image'
              sh 'chmod 755 cmp/collectors/ucs-cseries/build.sh'
                        sh './cmp/collectors/ucs-cseries/build.sh'
                    }
                }
            }

        stage('Build ucs-fi') {
            when {
                expression { ucsfifolder == '[cmp/collectors/ucs-fi]' }
            }
            steps {
                script { 
                        echo 'Building and Uploading the ucs-fi docker image'
              sh 'chmod 755 cmp/collectors/ucs-fi/build.sh'
                        sh './cmp/collectors/ucs-fi/build.sh'
                    }
                }
            }

        stage('Build telegraf') {
            when {
                expression { telegraffolder == '[cmp/collectors/telegraf]' }
            }
            steps {
                script { 
                        echo 'Building and Uploading the telegraf docker image'
              sh 'chmod 755 cmp/collectors/telegraf/build.sh'
                        sh './cmp/collectors/telegraf/build.sh'
                    }
                }
            }

        stage('Deployment of grafana_dashboards') {
            when {
                expression { grafanadashboardsfolder == '[cmp/visualization/grafana_dashboards]' }
            }
            steps {
                script { 
                        echo 'Deploying the grafana-dashboards'
                    }
                }
            }
        }
    }


  -  Python file for Folder identification
  
            import os
            import subprocess

            git_cmd='git diff-tree --no-commit-id --name-only -r HEAD'
            list1=[]

            commit_msg = subprocess.check_output(git_cmd, shell=True)
            for char in commit_msg:
                    list1.append(char)
            list2 = ''.join(list1).split('\n')

            print list2
            #git_file_path=list2[0]
            #dir= os.path.dirname(git_file_path)

            #print dir

            with open("folder_list.txt","w") as wfile:
                for item in list2:
                    print item
                    dir =os.path.dirname(item)
                    wfile.write(dir)
                    wfile.write("\n")

            with open("folder_list.txt","r") as rfile:
                rfile.read()




  - List out the Pull Request 

          git ls-remote origin 'pull/*/head'

  - List out the changed files in PR

           git diff-tree --no-commit-id --name-only -r 5be188c67cb1bc67df674095bc7896b512b7f8ba ( PR ID )
           
