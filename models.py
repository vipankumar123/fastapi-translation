from sqlalchemy import Column, Integer, String
from database import Base


class Leads(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String)
    work_phone = Column(String)


