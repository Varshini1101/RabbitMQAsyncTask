import pika
import json 

def pushmsg(feedback,feedbackid):
    thisdict={
        "feedback":feedback,
        "feedbackid":feedbackid

    }
    return thisdict
msg=pushmsg("nice idea!",1)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='feedbacks')
channel.basic_publish(exchange='', routing_key='feedbacks', body=json.dumps(msg))
print(msg)
connection.close()

    


         