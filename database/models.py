from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
DATABASE_URI = "postgres+psycopg2://postgres:password@localhost:5432/adnetwork"


def connect_db():
    db = create_engine("sqlite:///csv_test.db")
    return db


Base = declarative_base()


class AdNetwork(Base):
    __tablename__ = "daily_report"
    id = Column(Integer, primary_key=True)
    date = Column(String)
    app = Column(String)
    platform = Column(String)
    requests = Column(Integer)
    impressions = Column(Integer)
    revenue = Column(String)

    def __repr__(self):
        return "<adNetwork(date='{}', app='{}', platform={}, requests={}, impressions={}, revenue={})>".format(
            self.date,
            self.app,
            self.platform,
            self.requests,
            self.impressions,
            self.revenue,
        )


engine = connect_db()
AdNetwork.__table__.create(bind=engine, checkfirst=True)
