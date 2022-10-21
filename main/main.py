from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

@app.route('/')
def index():
    return 'Hello there'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')