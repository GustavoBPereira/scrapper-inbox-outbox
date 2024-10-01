from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite3')

Session = sessionmaker(bind=engine)
session = Session()

from app.infra.db.tables import Base
Base.metadata.create_all(engine)
