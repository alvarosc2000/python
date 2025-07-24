import os
from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base # type: ignore

sqllite_name = 'books.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))
database_url = f'sqlite:///{os.path.join(base_dir,sqllite_name)}'

engine = create_engine(database_url,echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()