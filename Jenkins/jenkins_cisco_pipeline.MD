## Jenkins Pipeline





  - List out the Pull Request 

          git ls-remote origin 'pull/*/head'

  - List out the changed files in PR

           git diff-tree --no-commit-id --name-only -r 5be188c67cb1bc67df674095bc7896b512b7f8ba ( PR ID )
           
