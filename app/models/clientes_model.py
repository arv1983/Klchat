from . import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from werkzeug.security import check_password_hash, generate_password_hash

class Clientes(db.Model):
    __tablename__="clientes"

    cliente_id = Column(Integer, primary_key=True)

    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    cpf = Column(String(11))
    cnpj = Column(String(14))
    telefone = Column(String(11), nullable=True)

    endereco_id = Column(Integer, ForeignKey("endereco.endereco_int") , nullable=False)

    cliente_endereco = relationship("Endereco", backref=backref("endereco_cliente"))

    @property
    def password(self):
        return {"Error password cannot be accessed"}
    @password.setter
    def create_password(self, password):
        self.senha = generate_password_hash(password=password, salt_length=10)

    def check_password(self, password_compare):
        return check_password_hash(self.senha, password_compare)
    
