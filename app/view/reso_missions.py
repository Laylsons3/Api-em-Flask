from flask_restful import Resource, reqparse
from flask import jsonify
from app.models.missions import Missions

class Index(Resource):
  def get(self):
    return jsonify("Bem vindo a aplicação Flask")

argumentos = reqparse.RequestParser()
argumentos.add_argument('mission_name', type=str)
argumentos.add_argument('lancamento', type=str)
argumentos.add_argument('destino', type=str)
argumentos.add_argument('estado', type=str)
argumentos.add_argument('tripulacao', type=str)
argumentos.add_argument('carga', type=str)
argumentos.add_argument('duracao', type=str)
argumentos.add_argument('custo', type=float)
argumentos.add_argument('status', type=str)

class MissionCreate(Resource):
  def post(self):
    try:
      dados = argumentos.parse_args()
      Missions.save_mission(self, dados['mission_name'], dados['lancamento'], dados['destino'], dados['estado'], dados['tripulacao'], dados['carga'], dados['duracao'], dados['custo'], dados['status'])
      return jsonify({"message": "Missão criada com sucesso"})
    except Exception as e:
      return jsonify({'message': 'Ocorreu um erro ao criar missão' })
    
argumentos_update = reqparse.RequestParser()
argumentos_update.add_argument('id', type=int)
argumentos_update.add_argument('mission_name', type=str)
argumentos_update.add_argument('lancamento', type=str)
argumentos_update.add_argument('destino', type=str)
argumentos_update.add_argument('estado', type=str)
argumentos_update.add_argument('tripulacao', type=str)
argumentos_update.add_argument('carga', type=str)
argumentos_update.add_argument('duracao', type=str)
argumentos_update.add_argument('custo', type=float)
argumentos_update.add_argument('status', type=str)

class MissionUpdate(Resource):
  def put(self):
    try:
      dados = argumentos.parse_args()
      Missions.update_mission(self, dados['id'], dados['mission_name'], dados['lancamento'], dados['destino'], dados['estado'], dados['tripulacao'], dados['carga'], dados['duracao'], dados['custo'], dados['status'])
      return jsonify({"message": "Missão atualizada com sucesso"})
    except Exception as e:
      return jsonify({'message': 'Ocorreu um erro ao atualizar missão' })

argumentos_delete = reqparse.RequestParser()
argumentos_delete.add_argument('id', type=int)

class MissionDelete(Resource):
  def delete(self):
    try:
      dados = argumentos_delete.parse_args()
      Missions.delete_mission(self, dados['id'])
      return jsonify({"message": "Missão deletada com sucesso"})
    except Exception as e:
      return jsonify({'message': 'Ocorreu um erro ao deletar missão' })

argumentos_list = reqparse.RequestParser()
argumentos_list.add_argument('id', type=int)

class MissionList(Resource):
  def get(self):
    try:
      dados = argumentos_list.parse_args()
      Missions.list_mission(self, dados['id'])
      return jsonify({"message": "Missão listada com sucesso"})
    except Exception as e:
      return jsonify({'message': 'Ocorreu um erro ao listar missão' })
    
argumentos_by_id = reqparse.RequestParser()
argumentos_by_id.add_argument('id', type=int)

class MissionById(Resource):
  def get(self):
    try:
      dados = argumentos_by_id.parse_args()
      Missions.list_mission(self, dados['id'])
      return jsonify({"message": "Missão listada com sucesso"})
    except Exception as e:
      return jsonify({'message': 'Ocorreu um erro ao listar missão' })