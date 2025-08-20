from sqlalchemy import Column, String, Boolean, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class CalculationSession(Base):
    __tablename__ = "calculation_session"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, unique=True, index=True, nullable=False)
    active = Column(Boolean, default=True)
    calculations = relationship("Calculation", back_populates="session")

class Calculation(Base):
    __tablename__ = "calculation"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, ForeignKey("calculation_session.session_id"))
    operation = Column(String)
    operand1 = Column(Float)
    operand2 = Column(Float)
    result = Column(Float)

    session = relationship("CalculationSession", back_populates="calculations")
