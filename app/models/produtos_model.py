from app.configs.database import db
from sqlalchemy import Column, String, Integer, ForeignKey


class Produtos(db.Model):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    descricao = Column(String(255), nullable=False)
    marca = Column(String(255), nullable=False)
    fabricante = Column(String(255), nullable=False)
    qtd_estoque = Column(Integer, nullable=False)
    logista_id = Column(Integer, ForeignKey(logista.id), nullable=False)
