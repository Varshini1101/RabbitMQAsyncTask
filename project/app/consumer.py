import pika, sys, os
import requests
import pymysql 
import json
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='feedbacks')

    def callback(ch, method, properties, body):
        a = json.loads(body)
        x = a["feedbackid"]
        #print("received")
        mydb= pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='EnterYourPassword', db='DatabaseName')
        #tag=requests.get("ModelAPI call")
        #tag="positive"
        mycursor = mydb.cursor()
        sql = "UPDATE feedback SET tag = %s WHERE id = %s"
        val=(tag,x)
        mycursor.execute(sql,val)
        mydb.commit()
       

    channel.basic_consume(queue='feedbacks', on_message_callback=callback, auto_ack=True)

   
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
