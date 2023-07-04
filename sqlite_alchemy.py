from sqlalchemy import create_engine,Column, Text, Integer
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('sqlite:///company.db')
Base = declarative_base()


# Table Already Existed Structure
class Employees(Base):
    __tablename__ = 'employees'
     
    rowid = Column(Integer,primary_key=True,autoincrement=True)
    user_name = Column(Text)
    email = Column(Text)
    address = Column(Text)
    password = Column(Text)


    def __init__(self, user_name,email,address,password):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.address = address


# if tablename doesn't exist, create new table in database
# Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


# Query all
def query_all(): 
    items = session.query(Employees).all()
    for item in items:
       print(item.rowid, item.user_name,item.email,item.address,item.password)


# filter some (eg.user name)
def filter_query():
    employees = session.query(Employees.user_name).all()  
    for employee in employees:
        print(employee[0])


# filter on condition
def filter_condition():
    user = session.query(Employees.user_name,Employees.address).filter(Employees.email == 'tony@gmail.com')
    for u in user: 
        print(f'Username: {u[0]}\nAddress: {u[1]}')


# Insert into table
def insert():
    user_name = input('Username: ')
    email = input("Email: ")
    address = input('Address: ')
    password = input('Password: ')
    emp = Employees(user_name,email, address, password)
    session.add(emp)
    session.commit()
    print('Details Added Successfully')


# Delete query on condition
def delete():
    rowid = int(input('Enter rowid: ')) 
    email = input('Enter email: ')
    emps =session.query(Employees).filter(Employees.rowid == rowid and Employees.email == email).one()
    session.delete(emps)
    session.commit()
    print('Detail Deleted Successfully')


# Update query
def update():
    rowid = int(input('Enter rowid: '))
    new_username = input("Enter new username: ")
    new_address = input("Enter new address: ")

    details = session.query(Employees).filter(Employees.rowid == rowid).one()
    details.user_name = new_username
    details.address = new_address
    session.commit()
    print('Details Updated Successfully')
    
    


def main():
    query_all()
   # filter_query()  
   # filter_condition()
   # insert()
   # delete()
   # update()


main()   

