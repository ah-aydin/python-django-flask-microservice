import pika
import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_service.settings')
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://fxmwjaah:plUKK_wGfsTMBsi9I8U3Sv6RSMTJO3Zt@rattlesnake.rmq.cloudamqp.com/fxmwjaah')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='product_service')

def callback(channel, method, properties, body):
    print('Got in product_service')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    print(method)
    if properties.content_type == 'product_liked':
        product.likes += 1
        print(f'liked product {id}')
    elif properties.content_type == 'product_unliked':
        product.likes -= 1
        print(f'unliked product {id}')
    product.save()

channel.basic_consume(queue='product_service', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()