## Git Commands to performe the operations

#### Configure the author name and email address to be used with your commits.

    git config --global user.name "Sam Smith"

    git config --global user.email sam@example.com

#### Create a new local repository

    git init

#### Check out a repository

 1. Create a working copy of a local repository:

           git clone /path/to/repository

 2. For a remote server, use:	
 
           git clone username@host:/path/to/repository
           
 ### Git Flow Diagram with commands
 
 ![image](https://github.com/learn-with-devops/devops/blob/master/images/Untitled%20Diagram.png)

## Branches

#### List out the branches
 
  1. List out remote branches

           git branch -r

  2. List out the local Branches

           git branch -a

 #### Create a Branch

           git checkout -b <branch-name>

 #### Switch from one branch to another

   			git checkout <branchname>

 #### Push a new branch to remote repository

   			git push --set-upstream origin <branch-name>

 #### Delete the feature branch

   			git branch -d <branchname>

 #### Push the branch to your remote repository, so others can use it

   			git push origin <branchname>

 #### Push all branches to your remote repository

		   git push --all origin

 #### Delete a branch on your remote repository

   			git push origin :<branchname>

   			git push origin --delete (branch name)

 #### Delete a branch on local repository

   			git branch -d (branch name)

  			 Note :  use -D for forcefully delete. 

 #### Create a "qa" branch and merge into "development" branch

            - git checkout -b qa
		    - do some modifications and commit
		    - git checkout development
		    - git pull origin development
		    - git merge qa
		    - git push origin development

 #### See the merging staructure on Graph

     		git log --all --graph

 #### To remove file from a repository

     		git rm README.md

 #### Git Tags
     

		     - git tag -l/--list
		     - git tag <tagname>   --for create
		     - git tag -am 'these tag is v2.4' v2.4
		     - git push origin development --tags
		     - git tag -d <tagname>   // for delete locally
		     - git push origin development :refs/tags/<tag name>
		     - git checkout v2.4.1 (for detached HEAD mode)

 #### Git fetch:
     
     
	      git pull = git fetch + git merge

	      git fetch == > will stores the info into u r local repo but it is not going to merge. For merging u need to run "git merge"
 
 #### git log

	       	For the graphical view of commits/logs

				git log --graph --decorate --oneline

				Note : If u want to see the specific commmit logs in graph format

				git log --graph  2291f4d

  
  #### Git Stash


          - git stash
		  - git stash (or) git stash save <file name>
		  - git stash apply
		  - git stash list
		  - git stash drop <stash id>
		  - git stash show stash@{0}

