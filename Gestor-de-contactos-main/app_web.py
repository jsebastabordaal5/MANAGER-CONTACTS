import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
import uvicorn

from src.controller.web_controlador import WebControlador

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "src", "view", "web")

if __name__ == "__main__":

    app = FastAPI()
    controlador = WebControlador()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(controlador.router)
    app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")


    uvicorn.run(app=app, host="127.0.0.1", port=8000)
