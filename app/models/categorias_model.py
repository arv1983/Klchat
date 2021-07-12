from sqlalchemy import Column, Integer, String
from . import db

class Categorias(db.Model):

    categoria_id = Column(Integer, primary_key=True)

    descricao = Column(String(255), nullable=False)