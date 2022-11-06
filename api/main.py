from datetime import datetime

import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from fastapi_sqlalchemy import DBSessionMiddleware, db

from db.schema import OD_Images
from db.schema import OD_Images as SchemaOD_Images
from db.models import OD_Images as ModelOD_Images

from ml.image_functions import post_azure_od, bound_image, upload_to_blob


app = FastAPI()

origins = [
  "http://localhost:8080"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)


@app.get("/test")
def test():
  return {"message": "Hello World"}


@app.post("/upload")
async def upload_image(file: UploadFile):
  try:
    contents = file.file.read()
    azure_response = await post_azure_od(contents)
    bounded_image = bound_image(contents, azure_response['objects'])
    azure_response["url"] = upload_to_blob(bounded_image, azure_response['requestId'])
    azure_response["time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # db_od_images = ModelOD_Images(modelVersion=OD_Images.modelVersion, url=OD_Images.url, requestID=OD_Images.requestID)
    # db.session.add(db_od_images)
    # db.session.commit()

    return azure_response
  except:
    return {"message": "There was an error uploading the file"}


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)