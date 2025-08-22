# db.py
import os
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1) читаем env с дефолтами (под твой compose)
DB_HOST = os.getenv("DB_HOST", "postgres_db")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "calculator")
DB_USER = os.getenv("DB_USER", "calculator_user")
DB_PASS = os.getenv("DB_PASS", "calculator_password")

# 2) allow override одной строкой (удобно для тестов/локали)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"postgresql+psycopg2://{DB_USER}:{quote_plus(DB_PASS)}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
)

# 3) создаём engine/Session (pool_pre_ping полезен при переподключениях)
engine = create_engine(DATABASE_URL, pool_pre_ping=True, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
