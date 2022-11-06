import cv2
import numpy as np
import httpx
import json

from azure.storage.blob import BlobServiceClient

from config import settings


async def post_azure_od(image):
  async with httpx.AsyncClient() as client:
    response = await client.post(
      'https://portfolio-object-detector.cognitiveservices.azure.com/vision/v3.2/detect',
      headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': settings.AZURE_API_KEY
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
  # Converted to np array
  np_array_image = np.frombuffer(byte_image, np.uint8)
  # Then convert to cv2 readable format
  image = cv2.imdecode(np_array_image, cv2.IMREAD_COLOR)
  for object in objects:
    x, y, w, h = object["rectangle"]["x"], object["rectangle"]["y"], object["rectangle"]["w"], object["rectangle"]["h"],
    image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
    text = object["object"] + ' ' + str(object["confidence"])
    cv2.putText(image, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
  # After drawing on image, encode to jpg
  processed_image = cv2.imencode('.jpg', image)[1].tobytes()
  return processed_image

def upload_to_blob(image, name):
  blob_service_client = BlobServiceClient.from_connection_string(settings.STORAGE_CONNECTION_STRING)
  blob_client = blob_service_client.get_blob_client(container='od-images', blob=name)
  blob_client.upload_blob(image)
  url = "https://portfolio094231.blob.core.windows.net/od-images/" + name
  return url