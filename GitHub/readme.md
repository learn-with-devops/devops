## Git Commands to performe the operations

#### Configure the author name and email address to be used with your commits.

    git config --global user.name "Sam Smith"

    git config --global user.email sam@example.com
    
    git config --list

#### Create a new local repository

    git init

#### Check out a repository

 1. Create a working copy of a local repository:

           git clone /path/to/repository

 2. For a remote server, use:	
 
           git clone username@host:/path/to/repository
           
 ### Git Flow Diagram with commands
 
 ![image](https://github.com/learn-with-devops/devops/blob/master/GitHub/images/GitHub_Flow.png)

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

			- To see top 2 logs with all commit info
				git log -p -2

  
  #### Git Stash


          - git stash
		  - git stash (or) git stash save <file name>
		  - git stash apply
		  - git stash list
		  - git stash drop <stash id>
		  - git stash show stash@{0}



- Git Rebase :

          -  Create a feature branch
             git checkout -b feature-branch

          -  Do some changes and commit to the local repository
             git commit -am "comment"

          -  Check out the branch which one you need to rebase
             git checkout master

          -  Performe the Rebase Operations
             git rebase feature-branch

          -  For verification please use below command
             gitk --all

          Note : 

          	- git rebase --abort
          	- git rebase --continue


- Git Diff

         	# See all (non-staged) changes done to a local repo
			$ git diff

			# See all (staged) changes done to a local repo
			$ git diff --cached

			# Check what the changes between the files you've committed and the live repo
			$ git diff --stat origin/master
			
			# Check the diff b/w two branches
			$ git diff stage master   ( for local branches)
			$ git diff origin/stage origin/master  ( for remote branches)
			
			

## Switching remote URLs from HTTPS to SSH

   Open Git Bash.

   Change the current working directory to your local project.

   List your existing remotes in order to get the name of the remote you want to change.

	$ git remote -v
	> origin  https://github.com/USERNAME/REPOSITORY.git (fetch)
	> origin  https://github.com/USERNAME/REPOSITORY.git (push)
	Change your remote's URL from HTTPS to SSH with the git remote set-url command.

	$ git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
	Verify that the remote URL has changed.

	$ git remote -v
	# Verify new remote URL
	> origin  git@github.com:USERNAME/REPOSITORY.git (fetch)
	> origin  git@github.com:USERNAME/REPOSITORY.git (push)


## Git Cherry-pick

	Cherry picking in Git means to choose a commit from one branch and apply it onto another.

	This is in contrast with other ways such as merge and rebase which normally apply many commits onto another branch.

		Make sure you are on the branch you want to apply the commit to.

			git checkout master
		
		Execute the following:
			
			git cherry-pick <commit-hash>
			

## Diff b/w Git and SVN

 1g. Distributed VCS								 
 1s. Centralized VCS
 2g. People have account to fork.Due to this, you can have all the information like logs, tags, history etc..  			 
 2s. don't have account to fork.
 3g. Create unlimited number of branches and very easy to merge .
 3s. Dificuly in mainatining of Multiple Number of branches and Meging is more dificult again.
 4g. If developer did mistake in Branch then PR cannot approved by Team.
 5g. SVN commit changes directly to main branch..So, if mistakes there then entire application will effect with that problem.
