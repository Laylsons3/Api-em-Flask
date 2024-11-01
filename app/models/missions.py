from app import db

class Missions(db.Model):
  __tablename__ = 'missions'
  __table_args__ = {'sqlite_autoincrement':True}
  id = db.Column(db.Integer, primary_key=True)
  mission_name = db.Column(db.String(255))
  lancamento = db.Column(db.String(255))
  destino = db.Column(db.String(255))
  estado = db.Column(db.String(255))
  tripulacao = db.Column(db.String(255))
  carga = db.Column(db.String(255))
  duracao = db.Column(db.String(255))
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
      mission = db.session.query(Missions).all()
      mission_dict = [{'id': missions.id, 'mission_name': missions.mission_name, 'lancamento': missions.lancamento, 'destino': missions.destino, 'estado': missions.estado, 'tripulacao': missions.tripulacao, 'carga': missions.carga, 'duracao': missions.duracao, 'custo': missions.custo, 'status': missions.status} for missions in mission]
      return mission_dict
    except Exception as e:
      print(e)
  
  def update_mission(self, id, mission_name, lancamento, destino, estado, tripulacao, carga, duracao, custo, status):
    try:
      db.session.query(Missions).filter(Missions.id == id).update({"mission_name": mission_name, "lancamento": lancamento, "destino": destino, "estado": estado, "tripulacao": tripulacao, "carga": carga, "duracao": duracao, "custo": custo, "status": status})
      db.session.commit()
    except Exception as e:
      print(e)
  
  def delete_mission(self, id):
    try:
      db.session.query(Missions).filter(Missions.id == id).delete()
      db.session.commit()
    except Exception as e:
      print(e)
  