from sqlalchemy import create_engine, Column,TIMESTAMP, String,Integer,Table,MetaData, text
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:chipsatony2002@Localhost:3306/sakila')

class Actor(Base):
    __tablename__ = 'actor'

    
    actor_id = Column(Integer ,primary_key=True, autoincrement=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    last_update = Column(TIMESTAMP)
    


# Base.metadata.create_all(bind=engine)
 
Session = sessionmaker(bind=engine)
session = Session()

actors =session.query(Actor.actor_id, Actor.first_name).order_by(Actor.first_name).all()
for actorid,firstname in actors:
   print(f'{actorid}. {firstname}' )

# update = session.query(Actor).all()

# count = 0
# for u in update:
#     count += 1
#     print(f'Employee # {count}')
#     print(f'Name: {u.first_name}  Last updated: {u.last_update}')
#     print()

