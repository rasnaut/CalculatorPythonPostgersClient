from sqlalchemy.orm import Session
import models

def create_session(db: Session, session_id: str):
    db_session = models.CalculationSession(session_id=session_id)
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

def get_calculations(db: Session, session_id: str):
    return db.query(models.Calculation).filter(models.Calculation.session_id == session_id).all()

def save_calculation(db: Session, session_id: str, operation: str, operand1: float, operand2: float, result: float):
    db_calculation = models.Calculation(
        session_id=session_id,
        operation=operation,
        operand1=operand1,
        operand2=operand2,
        result=result
    )
    db.add(db_calculation)
    db.commit()
    db.refresh(db_calculation)
    return db_calculation

def close_session(db: Session, session_id: str):
    db_session = db.query(models.CalculationSession).filter(models.CalculationSession.session_id == session_id).first()
    if db_session:
        db_session.active = False
        db.commit()
        db.refresh(db_session)
    return db_session
