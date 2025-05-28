from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from lib.db.connection import Base

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    rate = Column(Float)
    deadline = Column(Date)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)

    client = relationship('Client', back_populates='projects')
    invoices = relationship('Invoice', back_populates='project', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Project(name={self.name}, deadline={self.deadline})>"
