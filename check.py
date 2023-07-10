from sqlalchemy import create_engine, Column, Integer, String, DefaultClause
from sqlalchemy.schema import UniqueConstraint, CheckConstraint, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Mapped

# returns base class for declarative class definitions
# used as superclass for models
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'Customer'

    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    first_name = Column("FirstName", String(255), nullable=False)
    last_name = Column("LastName", String(255))
    address = Column('Address', String(255))
    age = Column('Age', Integer, CheckConstraint('age >= 10'))
    city = Column('City', String(255))  # default=DefaultClause('"Accra'))

    def __init__(self, id, first_name, last_name, address, age, city):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.age = age
        self.city = city

    def __repr__(self):
        return f'First Name: {self.first_name}\n' \
               f'Last Name: {self.last_name}\n' \
               f'Address:{self.address}\n' \
               f'Age: {self.age}\n' \
               f'City: {self.city}'


class Items(Base):
    __tablename__ = 'Items'

    description = Column('Description', String(255))
    telephone = Column('Order ID', String, primary_key=True)
    customer_id = Column("Customer ID", Integer, ForeignKey('Customer.ID'))
    price = Column('Price', Integer, nullable=False)

    # __table_args__ = (
    #   PrimaryKeyConstraint('description', 'order_id'),
    #  UniqueConstraint('order_id',
    #                  'description'))

    def __int__(self, descript, customer_id, price, order_id):
        self.description = descript
        self.customer_id = customer_id
        self.price = price
        self.order_id = order_id

    def __repr__(self):
        return f'Description: {self.description}\n' \
               f'Price: ${self.price}'


engine = create_engine('mysql+mysqlconnector://root:chipsatony2002@Localhost:3306/clients_db')
# engine = create_engine('sqlite:///mydb.db', echo=False)
# Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

customers = session.query(Customer).all()
print(customers)

