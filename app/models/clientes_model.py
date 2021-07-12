from . import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

class Clientes(db.Model):
    __tablename__="clientes"

    cliente_id = Column(Integer, primary_key=True)

    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    cpf = Column(String(11))
    cnpj = Column(String(14))
    telefone = Column(String(11), nullable=False)

    endereco_id = Column(Integer, ForeignKey("endereco.endereco_int") , nullable=False)

    cliente_enderco = relationship("Endereco", backref=backref("endereco_cliente"))

