from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
api = Api(app)
db = SQLAlchemy(app)

from app.models.missions import Missions
with app.app_context():
  db.create_all()

from app.view.reso_missions import MissionCreate, MissionUpdate, MissionDelete, MissionById, MissionList
api.add_resource(MissionCreate, "/")
api.add_resource(MissionUpdate, "/")
api.add_resource(MissionDelete, "/")
api.add_resource(MissionById, "/")
api.add_resource(MissionList, "/all")
