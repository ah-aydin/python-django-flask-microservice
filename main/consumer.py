import pika

params = pika.URLParameters('amqps://fxmwjaah:plUKK_wGfsTMBsi9I8U3Sv6RSMTJO3Zt@rattlesnake.rmq.cloudamqp.com/fxmwjaah')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(channel, method, properties, body):
    print('Got in consumer')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

channel.close()