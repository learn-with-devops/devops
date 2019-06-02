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

 ## Git Merge

 ####


