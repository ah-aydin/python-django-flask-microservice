import pika

params = pika.URLParameters('amqps://fxmwjaah:plUKK_wGfsTMBsi9I8U3Sv6RSMTJO3Zt@rattlesnake.rmq.cloudamqp.com/fxmwjaah')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method=None, body=None):
    channel.basic_publish(exchange='', routing_key='main', body='hello there')