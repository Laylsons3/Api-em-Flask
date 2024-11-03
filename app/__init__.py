from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
api = Api(app)
db = SQLAlchemy(app)
# from app.models.products import Products
from app.models.missions import Missions
with app.app_context():
  db.create_all()

# from app.view.reso_products import Index, ProductCreate, ProductUpdate, ProductDelete
# api.add_resource(Index, "/")
# api.add_resource(ProductCreate, "/")
# api.add_resource(ProductUpdate, "/")
# api.add_resource(ProductDelete, "/")

from app.view.reso_missions import MissionCreate, MissionUpdate, MissionDelete, MissionById, MissionList
api.add_resource(MissionCreate, "/")
api.add_resource(MissionUpdate, "/")
api.add_resource(MissionDelete, "/")
api.add_resource(MissionById, "/")
api.add_resource(MissionList, "/")


'''@app.route('/index')
def index():
    # return "<h1>Minha aplicação em Flask</h1>"
    return render_template('index.html')'''
