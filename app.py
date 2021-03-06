import os

from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identify
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
            os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'hiuu'
api = Api(app)

jwt = JWT(app, authenticate, identify)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')  # 127.0.0.1:5000
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/stores')

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
    # app.run(port=5000, debug=True, host='0.0.0.0')
