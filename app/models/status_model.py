from sqlalchemy import Integer, Column, String
from dataclasses import dataclass


from app.configs.database import db


@dataclass
class Status(db.Model):
    id: int
    situacao: str

    __tablename__ = "status"

    id = Column(Integer, primary_key=True)

    situacao = Column(String(255), nullable=False)
