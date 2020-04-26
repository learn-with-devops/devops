## DJango

### Installation

    pip install django==2.1
    
### create a Project

    django-admin startproject myapp .
    
### Run the Project

    python manage.py runserver
    
### Access the Django application like below

    http://localhost:8000/


## DJango-NewApp

### Create an App

        python manage.py startapp products
        
## View-Function  ( Used to navigate the page how the customer want like /products )

    viwes.py
    
            from django.shortcuts import render
            from django.http import HttpResponse


            # Create your views here.


            def index(request):
                return HttpResponse("This is Products Page !!")

## URL's Mapping


