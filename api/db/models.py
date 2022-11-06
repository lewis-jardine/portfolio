from sqlalchemy import Column, DateTime, Integer, String 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

class OD_Images(Base):

  __tablename__ = 'od_images'

  id = Column(Integer, primary_key=True, index=True)
  objects = Column(JSONB)
  modelVersion = Column(String)
  requestID = Column(String)
  url = Column(String)
  time_uploaded = Column(DateTime(timezone=True), server_default=func.now())