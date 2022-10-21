import pika
import json
from main import app, db, Product

params = pika.URLParameters('amqps://fxmwjaah:plUKK_wGfsTMBsi9I8U3Sv6RSMTJO3Zt@rattlesnake.rmq.cloudamqp.com/fxmwjaah')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(channel, method, properties, body):
    if not body:
        return
    data = json.loads(body)
    print(data)

    with app.app_context():
        if properties.content_type == 'product_created':
            product = Product(id=data['id'], title=data['title'], image=data['image'])
            db.session.add(product)
            db.session.commit()
            print('Product created')
        elif properties.content_type == 'product_updated':
            product = Product.query.get(data['id'])
            product.title = data['title']
            product.image = data['image']
            db.session.commit()
            print('Product updated')
        elif properties.content_type == 'product_deleted':
            product = Product.query.get(data)
            db.session.delete(product)
            db.session.commit()
            print('Product deleted')

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()