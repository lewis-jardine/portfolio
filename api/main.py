import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import httpx
import asyncio
import json

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

async def od_image(image):
  async with httpx.AsyncClient() as client:
    response = await client.post(
      'https://portfolio-object-detector.cognitiveservices.azure.com/vision/v3.2/detect',
      headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': '54ba7a81141a4bf0a35a9d18fff17ba6'
      },
      params = {
        'model-version': 'latest'
      },
      data = image
      )
    print(response, flush=True)
    return json.loads(response.read())

@app.get("/test")
def test():
  return {"message": "Hello World"}

@app.post("/upload")
async def upload_image(file: UploadFile):
  try:
    contents = file.file.read()
    with open(file.filename, 'wb') as f:
      f.write(contents)
      azure_response = await od_image(contents)
  except:
    return {"message": "There was an error uploading the file"}
  finally:
    file.file.close()
  return azure_response


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)