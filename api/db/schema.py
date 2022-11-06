from pydantic import BaseModel

class OD_Images(BaseModel):
  modelVersion: str
  requestID: str
  url: str