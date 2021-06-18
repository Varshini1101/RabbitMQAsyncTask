# RabbitMQAsyncTask
Required Installations:

> pip install pika

> pip install requests

> pip install mysqlclient

> pip install PyMySQL

> install Erlang from : https://www.erlang.org/downloads (choose OTP 24.0 Windows 64-bit Binary File )

> install RabbitMQ from : https://www.rabbitmq.com/install-windows.html (choose rabbitmq-server-3.8.17.exe)

To start RabbitMQ server :go to rabbitMQ Command Prompt and type rabbitmq-server start (this will start RabbitMQ server)

Run the COde:
> Select upto app folder and run python producer.py (this will send the data to RabbitMQ )
                                 python consumer.py (consumer takes the data present in the RabbitMQ and will update the tag in MYSQL)
                                 
RabbitMQ server runs at : localhost:15672 (Refer images)



 
