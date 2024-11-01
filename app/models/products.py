from app import db

class Products(db.Model):
  __tablename__ = 'products'
  __table_args__ = {'sqlite_autoincrement':True}
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  price = db.Column(db.Float)

  def __init__(self, name, price):
    self.name = name
    self.price = price

  def list_id(self, pruduct_id):
    try:
      product = db.session.query(Products).filter(Products.id == pruduct_id).all()
      products_dict = [{'id': products.id, 'name': products.name} for products in product]
      return products_dict
    except Exception as e:
      print(e)

  def save_products(self, name, price):
    try:
      add_banco = Products(name, price)
      db.session.add(add_banco)
      db.session.commit()
    except Exception as e:
      print(e)

  def update_product(self, id, name, price):
    try:
      db.session.query(Products).filter(Products.id == id).update({"name": name, "price": price})
      db.session.commit()
    except Exception as e:
      print(e)

  def delete_products(self, id):
    try:
      db.session.query(Products).filter(Products.id == id).delete()
      db.session.commit()
    except Exception as e:
      print(e)
  