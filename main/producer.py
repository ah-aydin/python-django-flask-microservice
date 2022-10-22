import pika
import json

params = pika.URLParameters('amqps://fxmwjaah:plUKK_wGfsTMBsi9I8U3Sv6RSMTJO3Zt@rattlesnake.rmq.cloudamqp.com/fxmwjaah')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(content_type=method)
    channel.basic_publish(exchange='', routing_key='product_service', body=json.dumps(body), properties=properties)