from sqlalchemy import Column, Integer, String
from dataclasses import dataclass

from app.configs.database import db


@dataclass
class Categorias(db.Model):
    id: int
    descricao: str

    __tablename__="categorias"
    
    id = Column(Integer, primary_key=True)

    descricao = Column(String(255), nullable=False)
