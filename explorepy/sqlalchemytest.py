from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base as ds, declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Define a model
class usersvenky(Base):
    __tablename__ = 'usersvenky'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create an engine and connect to the PostgreSQL database
# engine = create_engine('postgresql+psycopg2://username:password@hostname/database_name')
engine = create_engine('postgresql+psycopg2://postgres:log@localhost/zishta2024dump')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user
new_user = usersvenky(name='Alice', age=25)
session.add(new_user)
session.commit()

# Query the database
users = session.query(usersvenky).all()
for user in users:
    print(user.name, user.age)
