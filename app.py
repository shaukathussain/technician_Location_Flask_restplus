from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
#from flask_sqlalchemy import SQLAlchemy
#import sqlite3
from resources.skill import Skill, SkillList
from security import authenticate, identity
from resources.user import UserRegister
from resources.worker import Worker, WorkerList
from resources.workermobupdate import WorkerMobUpdate
from resources.rating import Rating
from db import db
import urllib


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1/new_kam'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'shaukat'  # this key has to be secret and some long string
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Skill, '/skill/<string:name>')
api.add_resource(SkillList, '/skills')
api.add_resource(Worker, '/worker/<string:mobNum>')
api.add_resource(WorkerMobUpdate, '/workermobupdate/<int:workerId>')
api.add_resource(WorkerList, '/workers')
api.add_resource(Rating, '/rating/int:workerId')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=8000, debug=True)
