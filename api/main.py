import json

import uvicorn
import httpx
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import cv2
import numpy as np

from azure.storage.blob import BlobServiceClient

import config


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

async def post_azure_od(image):
  async with httpx.AsyncClient() as client:
    response = await client.post(
      'https://portfolio-object-detector.cognitiveservices.azure.com/vision/v3.2/detect',
      headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': config.AZURE_API_KEY
      },
      params = {
        'model-version': 'latest'
      },
      data = image
      )
    print(response, flush=True)
    return json.loads(response.read())

def bound_image(byte_image, objects):
  # Image initaially byte string
  for object in objects:
    # Converted to np array
    image = np.frombuffer(byte_image, np.uint8)
    x, y, w, h = object["rectangle"]["x"], object["rectangle"]["y"], object["rectangle"]["w"], object["rectangle"]["h"],
    image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
    cv2.putText(image, object["object"], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
  # Convert back to byte string
  processed_image = image.tobytes()
  return processed_image

def upload_to_blob(image, name):
  blob_service_client = BlobServiceClient.from_connection_string(config.STORAGE_CONNECTION_STRING)
  blob_client = blob_service_client.get_blob_client(container='od-images', blob=name)
  blob_client.upload_blob(image)


@app.get("/test")
def test():
  return {"message": "Hello World"}

@app.post("/upload")
async def upload_image(file: UploadFile):
  try:
    contents = file.file.read()
    azure_response = await post_azure_od(contents)
    bounded_image = bound_image(contents, azure_response['objects'])
    upload_to_blob(bounded_image, azure_response['requestId'])

    return {"response": azure_response}
  except:
    return {"message": "There was an error uploading the file"}


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)