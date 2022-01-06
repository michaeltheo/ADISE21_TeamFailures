from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL='postgresql://ctatstkjmjqtex:413949579933eec9393c9eab104e55b9fd62a5c5aa72de5b34e8e65c3eb83858@ec2-54-229-68-88.eu-west-1.compute.amazonaws.com:5432/d5pv25rpn5docu'
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})
Base=declarative_base()
SessionLocal=sessionmaker(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
