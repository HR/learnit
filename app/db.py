
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from app import app
from models import Base

# app.config.from_pyfile('config.py')
#db = SQLAlchemy(app)

engine = create_engine('sqlite:///salaries.db')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=engine)
session = scoped_session(Session)
