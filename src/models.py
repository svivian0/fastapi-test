from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey #permite conectar uma tabela em outras #import the columns and the types of then
from sqlalchemy.orm import declarative_base


##BASE STRUCTURE
#create the conection of db
db = create_engine("sqlite:///../data/database.db")


#create the base of db
base = declarative_base()

class user(base):  ## in SQLAlchemy a class turn a table
    __tablename__ = 'users' ##the ofc name of this table in the db
    id= Column("id", Integer, primary_key=True, nullable=False, autoincrement=True) #turn the id impossible to stay null
    name = Column("name", String(150), nullable=False)
    email = Column("email", String(150), nullable=False, unique=True) #turn the email unique, two user cant use the same email
    password = Column("password", String(255), nullable=False) #turn the password impossible to stay null
    date = Column("date", String, nullable=False) 
    adm = Column("adm", Boolean, default=False) #do a new user, per default, a non admin, unless you define it as True
    phone = Column("phone", String)

    def __init__(self, name, email, password, date, adm=False, phone=None): #função init define os estados iniciais da classe
        self.name = name
        self.email = email
        self.password = password
        self.date = date
        self.adm = adm
        self.phone = phone
