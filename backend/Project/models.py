


from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String


class User(Base):
    __tablename__='Users'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
