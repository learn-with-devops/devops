# NPM

## What is NPM ??

        NPM is a package manager for Node.js packages, or modules if you like.

        www.npmjs.com hosts thousands of free packages to download and use.

        The NPM program is installed on your computer when you install Node.js
        
   Node Package Manager (NPM) provides two main functionalities −

         - Online repositories for node.js packages/modules which are searchable on search.nodejs.org

         - Command line utility to install Node.js packages, do version management and dependency management of Node.js packages.
        

## NPM Commands 

   To verify the NPM ??
   
        $ npm --version
          2.7.1
          
   Want to update the NPM ??
   
        npm install npm@latest -g
        
   List out the Packages ??
      
        npm list
        
   List Out the global packages ??
     
        npm list --global

   Installing Packages in Local Mode ??
     
        npm init  //package.json required for this
        
   Install any Module/Packages ??
   
        npm install express  // express is a package
        
   Install a Module/package globally??
   
        npm install express -g
        
   Uninstall a Module ??
    
        npm uninstall express
    
   Update a Module ?
   
        npm update express
        
   Search a Module ??
   
        npm search express
        
   Download all the dependencies specified in the Package.json file ??
       
        npm install
        
### What is a package.json file?

        At its simplest, a package.json file can be described as a manifest of your project that includes the packages and applications it depends on, information about its unique source control, and specific metadata like the project's name, description, and author.
   
   
   Example : 
             
             {
                  "name": "metaverse",
                  "version": "0.92.12",
                  "description": "The Metaverse virtual reality. The final outcome of all virtual worlds, augmented reality, and the Internet.",
                  "main": "index.js"
                  "license": "MIT",
                  "devDependencies": {
                    "mocha": "~3.1",
                    "native-hello-world": "^1.0.0",
                    "should": "~3.3",
                    "sinon": "~1.9"
                  },
                  "dependencies": {
                    "fill-keys": "^1.0.2",
                    "module-not-found-error": "^1.0.0",
                    "resolve": "~1.1.7"
                  }
                }
