from dataclasses import dataclass
import requests
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate
from producer import publish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)

@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id: int
    user_id: int
    product_id: int
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    db.UniqueConstraint('user_id', 'product_id', name='user_product_unique')

migrate = Migrate(app, db)

@app.route('/api/products')
def index():
    return jsonify(Product.query.all())

@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://docker.for.mac.localhost:7000/api/users')
    json = req.json()
    productUser = ProductUser.query.filter_by(user_id=json['id'], product_id=id).first()
    try:
        if productUser:
            raise Exception('Product exists')
        productUser = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()

        # event
        publish('product_liked', id)
    except Exception:
        db.session.delete(productUser)
        db.session.commit()
        publish('product_unliked', id)
        return jsonify({
            'message': f'unliked {json["id"]}',
        })

    return jsonify({
        'message': f'liked {json["id"]}',
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')