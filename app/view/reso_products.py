from flask_restful import Resource, reqparse
from flask import jsonify
from app.models.products import Products

class Index(Resource):
  def get(self):
    return jsonify("Bem vindo a aplicação Flask")
  

class ProductById(Resource):
  def get(self):
    try:
      print("lascou")
    except Exception as e:
      print("lascou")



argumentos = reqparse.RequestParser()
argumentos.add_argument('name', type=str)
argumentos.add_argument('price', type=float)

class ProductCreate(Resource):
  def post(self):
    try:
      dados = argumentos.parse_args()
      Products.save_products(self, dados['name'], dados['price'])
      return jsonify({"message": "Produto criado com sucesso"})
    except Exception as e:
      return jsonify({'message': 'Ocorreu um erro ao tentar criar um produto' })

argumentos_update = reqparse.RequestParser()
argumentos_update.add_argument('id', type=int)
argumentos_update.add_argument('name', type=str)
argumentos_update.add_argument('price', type=float)

class ProductUpdate(Resource):
  def put(self):
    try:
      dados = argumentos_update.parse_args()
      Products.update_product(self, dados['id'], dados['name'], dados['price'])
      return jsonify({"message": "Produto atualizado com sucesso"})
    except Exception as e:
      return jsonify({'message': 'Ocorreu um erro ao tentar atualizar o produto' })

argumentos_delete = reqparse.RequestParser()
argumentos_delete.add_argument('id', type=int)

class ProductDelete(Resource):
  def delete(self):
    try:
      dados = argumentos_delete.parse_args()
      Products.delete_products(self, dados['id'])
      return jsonify({"message": "Produto deletado com sucesso"})
    except Exception as e:
      return jsonify({'message': 'Ocorreu um erro ao tentar deletar o produto' })
