import pika

params = pika.URLParameters('amqps://fxmwjaah:plUKK_wGfsTMBsi9I8U3Sv6RSMTJO3Zt@rattlesnake.rmq.cloudamqp.com/fxmwjaah')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(channel, method, properties, body):
    print('Got in product_service')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()