from flask import Flask, request, jsonify
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud
import models

app = Flask(__name__)

# Creation tables in db
models.Base.metadata.create_all(bind=engine)

@app.route('/api/sessions/<session_id>/create', methods=['POST'])
def create_session_endpoint(session_id):
    print("! Create Session !")
    with SessionLocal() as db:
        session = crud.create_session(db, session_id)
    return jsonify(session_id=session.session_id, active=session.active), 201

@app.route('/api/sessions/<session_id>/get_calculations', methods=['GET'])
def get_calculations_endpoint(session_id):
    with SessionLocal() as db:
        calculations = crud.get_calculations(db, session_id)
    return jsonify([calculation.__dict__ for calculation in calculations])

@app.route('/api/sessions/<session_id>/save_calculations', methods=['POST'])
def save_calculation_endpoint(session_id):
    data = request.json
    with SessionLocal() as db:
        calculation = crud.save_calculation(db, session_id, data['operation'], data['operand1'], data['operand2'], data['result'])
    return jsonify(calculation.__dict__), 201

@app.route('/api/sessions/<session_id>/close', methods=['POST'])
def close_session_endpoint(session_id):
    with SessionLocal() as db:
        session = crud.close_session(db, session_id)
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
