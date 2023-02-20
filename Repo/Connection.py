import sqlalchemy as orm
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

engine = orm.create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/intern")

db = scoped_session(sessionmaker(bind=engine))
# Base.query= db.query_property()
class _Base(object):
    query= db.query_property()

Base = declarative_base(cls=_Base)