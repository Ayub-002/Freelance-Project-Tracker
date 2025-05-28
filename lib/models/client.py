from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.connection import Base

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String)

    projects = relationship('Project', back_populates='client', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Client(name={self.name}, email={self.email})>"
