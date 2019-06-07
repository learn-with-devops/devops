  488  git clone https://github.com/jntu-college/login.git
  489  cd login/
  490  git config --list
  491  clear
  492  ls
  493  ls -ltr
  494  vi index.html
  495  git status
  496  cat index.html
  497  git checkout -- .
  498  cat index.html
  499  vi index.html
  500  git status
  501  cat index.html
  502  git add index.html
  503  cat index.html
  504  git status
  505  git reset --head
  506  git reset --hard
  507  cat index.html
  508  git commit -am "Added one more head with branch info"
  509  git status
  510  cat index.html
  511  git reset --hard head~1
  512  cat index.html
  513  clear
  514  git log
  515  git log -p -1
  516  q
  517  clear
  518  git log
  519  cat index.html
  520  git commit -am "Added one more head with branch info"
  521  git log
  522  git reset --soft head~1
  523  git status
  524  git reset --hard
  525  cat index.html
  526  clear
  527  git status
  528  git diff
  529  git add .
  530  git diff
  531  git diff --cached
  532  clear
  533  git status
  534  git reset --head
  535  git reset head
  536  git status
  537  git diff index.html
  538  vi README.md
  539  git status
  540  git diff
  541  git diff index.html
  542  clear
  543  git add .
  544  git commit -m "Latest changes "\
  545  git commit -m "Latest changes "
  546  git push origin master
  547  git push origin master
  548  clear
  549  git log
  550  clear
  551  git pull
  552  git branch
  553  git branch -r
  554  git branch -a
  555  git checkout -b feature-branch
  556  git branch -r
  557  git branch -a
  558  clear
  559  ls
  560  ls
  561  vi index.html
  562  git add .
  563  git commit -m "feature branch"
  564  git status
  565  git diff feature-branch dev
  566  git diff dev
  567  git diff master
  568  git diff master feature-branch
  569  clear
  570  git checkout dev
  571  ls
  572  git diff dev feature-branch
  573  git merge feature-branch
  574  cat index.html
  575  git push origin dev
  576  clear
  577  gitk --all
  578  git checkout -b stage
  579  vi index.html
  580  git commit -am "stage branch"
  581  git push --set-upstream origin stage
  582  gitk --all
  583  git log
  584  clear
  585  git branch -r
  586  git branch -a
  587  git branch -d feature-branch
  588  git branch -a
  589  git og
  590  git log
  591  git log --graph --all
  592  git log --graph --all --oneline
  593  history
