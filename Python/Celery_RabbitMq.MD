# RabbitMQ

RabbitMQ is an open-source message-broker software that originally implemented the Advanced Message Queuing Protocol and has since been extended with a plug-in architecture to support Streaming Text Oriented Messaging Protocol, Message Queuing Telemetry Transport, and other protocols.


   Connection from Cerely to RabbitMQ Output

        [2019-09-17 09:16:19,914: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
        [2019-09-17 09:16:19,923: INFO/MainProcess] mingle: searching for neighbors
        [2019-09-17 09:16:20,942: INFO/MainProcess] mingle: all alone


# Celery

Celery is an open source asynchronous task queue or job queue which is based on distributed message passing. While it supports scheduling, its focus is on operations in real time.



Process :
---------

  RabbitMQ Installation:

        - yum install rabbitmq-server
        - service rabbitmq-server restart
        - service rabbitmq-server status
        
        
  Celery Installation :
  
        - pip install celery  // Please install pytest
                  - pip install pytest
                  
  Code for Cerely :
  
          from celery import Celery

          app = Celery('tasks', borker='amqp://localhost//')

          @app.task
          def reverse(string):
            return string[::-1]
        
  Run the program with Celery:
  
          celery -A tasks worker --loglevel=info
          
          
  If you want to check the Asyncronus que execution they run like below :
  
          python
          from tasks import *
          reverse('anand') //Will get the output with reverse string
          
          Asynchronous Execution :
          
          reverse.delay('anand')
              >>> reverse.delay('anand')
                  <AsyncResult: 6409a59e-33a3-4478-b524-302974577ee9>
                  
                  
                  Output : 
                  
                  [2019-09-17 09:19:31,721: INFO/MainProcess] Received task: tasks.reverse[6409a59e-33a3-4478-b524-302974577ee9]
                  [2019-09-17 09:19:31,723: INFO/ForkPoolWorker-1] Task tasks.reverse[6409a59e-33a3-4478-b524-302974577ee9] succeeded in 0.000393608002923s: 'dnana'

      
        
Reference :

      https://www.youtube.com/watch?v=fg-JfZBetpM
      
      


