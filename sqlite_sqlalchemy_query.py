from sqlalchemy import create_engine, Column, Integer, String,ForeignKey,func
from sqlalchemy.orm import declarative_base, sessionmaker
import uuid


Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())
    

class Customers(Base):
      __tablename__ = 'Customers'

      customer_id = Column("customer_id", String(15),primary_key=True,default=generate_uuid)
      customer_name = Column("customer_name", String(255),nullable=False)
      email = Column("email", String(255), nullable=False)
      address = Column('address', String(255))

      def __init__(self,customer_name,email,address):
           self.customer_name = customer_name
           self.email = email
           self.address = address

      def __repr__(self):
           return f'Name: {self.customer_name}\nEmail: {self.email}\nAddress: {self.address}'

class Items(Base):
     __tablename__ = 'Items'

     itemid = Column("itemid", Integer, primary_key=True, autoincrement=True)
     description = Column('description', String(255)) 
     price = Column('price', Integer)          
     customer_id= Column('customer_id', String(15), ForeignKey('Customers.customer_id'))  

     def __init__(self, description,price, customer_id):
        self.description = description
        self.price = price
        self.customer_id = customer_id

     def __repr__(self):
          return f'{self.description} owned by {self.customer_id}\nPrice: ${self.price}'   


engine = create_engine('sqlite:///Store.db')
# Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()



# c1 = Customers('Tony Blair', 'tonyblair@gmail.com',"Sunyani")
# c2 = Customers('Cristiano Ronaldo', 'cr7@gmail.com',"Abu Dhabi")
# c3 = Customers('Lionel Messi', 'lm10@gmail.com', 'Miami')
# c4 = Customers('Kwaku Yeboah', 'kwakuyeboah@gmail.com', "Kumasi")

# session.add_all([c1,c2,c3,c4])
# session.commit()

# t1 = Items("Nike shoe", 150, c1.customer_id)
# t2 = Items("Nike shoe", 1000, c2.customer_id)
# t3 = Items("Adidas shoe", 1500, c3.customer_id)
# t4 = Items('Gucci bag', 300, c4.customer_id)
# t5 = Items('Balenciaga shirt', 1400, c1.customer_id)
# t6 = Items('Versace belt', 300, c2.customer_id)

# session.add_all([t1,t2,t3,t4,t5,t6])
# session.commit()


amounts = session.query(Customers.customer_name,Items.price).filter(Customers.customer_id == Items.customer_id)
for amount in amounts:
     print(amount)


# total = session.query(Customers.customer_name,func.sum(Items.price)).filter(Customers.customer_id == Items.customer_id).group_by(Customers.customer_name) 
# for name, price in total:
#      print(f'Name: {name}  Price: ${price}')


# amounts = (
#     session
#     .query(Customers.customer_name, func.sum(Items.price))
#     .filter(Customers.customer_id == Items.customer_id)
#     .group_by(Customers.customer_name)
# )

# for customer_name, total_price in amounts:
#     print(f"Customer: {customer_name}, Total Price: ${total_price}")