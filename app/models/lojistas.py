
from . import db
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash
class Lojistas(db.Model):
    __tablename__ = "logistas"
    id = Column(Text, nullable=False, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    cnpj = Column(String(14), nullable=False)
    telefone = Column(Integer, nullable=True)
    endereco_id = Column(Integer,ForeignKey("enderecos.id"), nullable=False)
    

    
    @property
    def password(self):
        return {"Error password cannot be accessed"}
    @password.setter
    def create_password(self, password):
        self.senha= generate_password_hash(password=password, salt_length=10)

    def check_password(self, password_compare):
        return check_password_hash(self.senha, password_compare)
    