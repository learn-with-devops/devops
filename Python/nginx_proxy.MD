# Nginx Reverse proxy configuration with Python API's

Program 1: 
----------

            from flask import Flask
            app = Flask(__name__)

            @app.route("/home")
            def main():
                return "Welcome!. This is Flask Test Part 1"

            if __name__ == "__main__":
                job_id = 1234
                app.run(host= '0.0.0.0')

    
      Run this: 

            export FLASK_APP=test1.py
            flask run --host 0.0.0.0 --port 5000
      
  
Program 2:
----------

            app = Flask(__name__)

            @app.route("/")
            def main():
                return "Welcome!. This is Flask Test Part 2"

            if __name__ == "__main__":
                job_id = 4321
                app.run(host= '0.0.0.0')

      Run this: 

            export FLASK_APP=test2.py
            flask run --host 0.0.0.0 --port 5001
   
   
   
   
   Reverse Proxy configuration:
   
                        upstream pythonweb {

                                    server localhost:5000;
                                    server localhost:5001;

                        }

                        server {

                                    listen 80;

                                    location /home {
                                    proxy_pass "http://pythonweb/home"
                                    }
                        }
