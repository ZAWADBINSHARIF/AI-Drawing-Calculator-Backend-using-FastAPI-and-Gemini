from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from constants import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"]
    # allow_credentials=True,
    # allow_method=["*"],
    # all_headers=["*"]
)


@app.get("/")
async def health():

    return {"message": f"Server is running..."}
