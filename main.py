# For running the FastAPI, write the command in the terminal
# uvicorn main:app --host 0.0.0.0 --port 4000

from io import BytesIO
from fastapi import FastAPI
import base64
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from PIL import Image

from schema import ImageData
from utilities import analyze_image


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081", "http://192.168.0.105:8081"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def health():

    return {"message": f"Server is running..."}


@app.post("/calculation")
async def calculation(data: ImageData):

    image_data = base64.b64decode(data.image)
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)
    responses = analyze_image(image, dict_of_vars=data.dict_of_vars)

    data = []
    for response in responses:
        data.append(response)

    # print("response in route: ", responses)
    return {"message": "Image processed", "data": data, "status": "success"}
