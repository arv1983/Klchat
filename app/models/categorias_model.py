from sqlalchemy import Column, Integer, String
from dataclasses import dataclass

from configs.database import db


@dataclass
class Categorias(db.Model):
    id: int
    descricao: str

    id = Column(Integer, primary_key=True)

    descricao = Column(String(255), nullable=False)
