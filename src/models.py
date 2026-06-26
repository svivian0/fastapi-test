from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


##BASE STRUCTURE
#create the conection of db
db = create_engine("sqlite:///../data/database.db")


#create the base of db
Base = declarative_base()

