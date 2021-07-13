
from . import db
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, backref

class Logistas(db.Model):
    __tablename__ = "lojistas"
    id = Column(Text, nullable=False, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    cnpj = Column(String(14), nullable=False)
    telefone = Column(Integer, nullable=False)
    endereco_id = Column(Integer,ForeignKey("enderecos.id"), nullable=False)




    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)
    eisenhower_id = Column(Integer, ForeignKey("eisenhowers.id"))