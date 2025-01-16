# For running the FastAPI, write the command in the terminal
# uvicorn main:app --host 0.0.0.0 --port 4000 --reload

import asyncio
from io import BytesIO
from fastapi import FastAPI
import base64
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from PIL import Image
import uvicorn
import uvicorn.config
import uvicorn.server
from constants.constants import settings

from schema import ImageData
from utilities.analyze_image import analyze_image


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def health():
    print(settings.GenKey)
    return {"message": f"Server is running..."}


@app.post("/calculation")
async def calculation(data: ImageData):

    image_data = base64.b64decode(data.image)
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)  # image_name.png

    responses = analyze_image(image, dict_of_vars=data.dict_of_vars)

    print(responses)

    data = []
    for response in responses:
        data.append(response)

    # print("response in route: ", responses)
    return {"message": "Image processed", "data": data, "status": "success"}


async def main():
    config = uvicorn.Config(
        "main:app", host="0.0.0.0", port=4000, log_level="info", reload=True
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
