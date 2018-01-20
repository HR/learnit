#!/usr/bin/env python
"""
models.py - 
"""


from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Data(Base):
    __tablename__ = 'knowledge_data'

    id = Column(Integer, primary_key=True)
    data = Column(String(9999))


class Questions(Base):
    __tablename__ = 'knowledge_questions'

    id = Column(Integer, primary_key=True)
    #data_id = Column(Integer)
    question = Column(String(100))

if __name__ == "__main__":
    pass
