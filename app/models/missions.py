from app import db
from sqlalchemy import desc

class Missions(db.Model):
  __tablename__ = 'missions'
  __table_args__ = {'sqlite_autoincrement':True}
  id = db.Column(db.Integer, primary_key=True)
  mission_name = db.Column(db.String(255))
  lancamento = db.Column(db.String(20))
  destino = db.Column(db.String(50))
  estado = db.Column(db.String(30))
  tripulacao = db.Column(db.String(255))
  carga = db.Column(db.String(255))
  duracao = db.Column(db.String(50))
  custo = db.Column(db.Float)
  status = db.Column(db.String(255))

  def __init__(self, mission_name, lancamento, destino, estado, tripulacao, carga, duracao, custo, status):
    self.mission_name = mission_name
    self.lancamento = lancamento
    self.destino = destino
    self.estado = estado
    self.tripulacao = tripulacao
    self.carga = carga
    self.duracao = duracao
    self.custo = custo
    self.status = status

  def save_mission(self, mission_name, lancamento, destino, estado, tripulacao, carga, duracao, custo, status):
    try:
      add_banco = Missions(mission_name=mission_name, lancamento=lancamento, destino=destino, estado=estado, tripulacao=tripulacao, carga=carga, duracao=duracao, custo=custo, status=status)
      db.session.add(add_banco)
      db.session.commit()
    except Exception as e:
      print(e)
  
  def list_mission(self):
      try:
          missions = db.session.query(Missions).order_by(desc(Missions.lancamento)).all()
          
          mission_dict = [
              {
                  'id': mission.id,
                  'mission_name': mission.mission_name,
                  'lancamento': mission.lancamento,
                  'destino': mission.destino,
                  'estado': mission.estado,
                  'tripulacao': mission.tripulacao,
                  'carga': mission.carga,
                  'duracao': mission.duracao,
                  'custo': mission.custo,
                  'status': mission.status
              }
              for mission in missions
          ]
          return mission_dict
      except Exception as e:
          print(e)

  
  def update_mission(self, id, mission_name=None, lancamento=None, destino=None, estado=None, tripulacao=None, carga=None, duracao=None, custo=None, status=None):
      try:
          fields_to_update = {
              "mission_name": mission_name,
              "lancamento": lancamento,
              "destino": destino,
              "estado": estado,
              "tripulacao": tripulacao,
              "carga": carga,
              "duracao": duracao,
              "custo": custo,
              "status": status
          }
          
          fields_to_update = {key: value for key, value in fields_to_update.items() if value is not None}

          if fields_to_update:
              db.session.query(Missions).filter(Missions.id == id).update(fields_to_update)
              db.session.commit()
          else:
              print("Nenhum campo para atualizar.")

      except Exception as e:
          print(f"Erro ao atualizar missão: {e}")

  
  def delete_mission(self, id):
    try:
      db.session.query(Missions).filter(Missions.id == id).delete()
      db.session.commit()
    except Exception as e:
      print(e)
