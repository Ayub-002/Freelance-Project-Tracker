from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from lib.db.connection import Base

class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    date_issued = Column(Date, nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)

    project = relationship('Project', back_populates='invoices')

    def __repr__(self):
      return f"<Invoice(amount={self.amount}, status={self.status})>"
