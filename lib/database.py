"""
Database
"""
from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from config.settings import Settings

Base = declarative_base()


def get_engine(settings: Settings) -> Engine:
    """Get database engine"""
    return create_engine(settings.SQLALCHEMY_DATABASE_URI)


def get_session(settings: Settings) -> Session:
    """Get database session"""
    engine = get_engine(settings)
    session_maker = sessionmaker(bind=engine)
    return session_maker()
