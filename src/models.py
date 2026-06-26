from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey #permite conectar uma tabela em outras #import the columns and the types of then
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType #permite passar apenas opções especificas para uma coluna


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
    datetime = Column("date", String, nullable=False) 
    adm = Column("adm", Boolean, default=False) #do a new user, per default, a non admin, unless you define it as True
    phone = Column("phone", String)

    def __init__(self, name, email, password, datetime, adm=False, phone=None): #função init define os estados iniciais da classe
        self.name = name
        self.email = email
        self.password = password
        self.date = datetime
        self.adm = adm
        self.phone = phone

class order(base):
    __tablename__ = "orders"
    id = Column("id", Integer, primary_key=True, nullable=False, autoincrement=True) #primary key torna esse pedido unico
    status= Column("status", ChoiceType([("PRONTO", "PRONTO"), ("PENDENTE", "PENDENTE"), ("CANCELADO", "CANCELADO")]), default="PENDENTE") # ChoiceType is like a restriction
    user_id= Column("user_id", ForeignKey("users.id"))#transforma o valor de user_id no id da tabela estrangeira users
    datetime= Column("datetime", String)
    price= Column("price", Float, nullable=False)

    def __init__(self, status, user_id, datetime, price=0):
        self.status = status
        self.user_id = user_id
        self.datetime = datetime
        self.price = price

class items_order(base):
    __tablename__ = "items_orders"
    id = Column("id", Integer, primary_key=True, nullable=False, autoincrement=True) #primary key torna esse pedido unico
    order_id = Column("order_id", ForeignKey("orders.id")) #transforma o valor de order_id no id da tabela estrangeira orders
    amount = Column("amount", Integer, default=0)
    price = Column("price", Float, nullable=False)
    topping = Column("topping", String(150), nullable=False)
    size = Column("size", ChoiceType([("SMALL", "SMALL"), ("MEDIUM", "MEDIUM"), ("LARGE", "LARGE")]), default="MEDIUM")

    def __init__(self, order_id, amount, price, topping, size):
        self.order_id = order_id
        self.amount = amount
        self.price = price
        self.topping = topping
        self.size = size