import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Initialize the FastAPI application instance
app = FastAPI()

# Define absolute paths to ensure the server finds the folder regardless of where it's executed
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Mount the static files directory to the "/imgs" route
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Define the list of stickers with their metadata and image URLs
figurinhas = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA", "imagem_url": "/imgs/01-alan-turing.jpg"},
    {"id": 2, "nome": "John McCarthy", "categoria": "IA", "imagem_url": "/imgs/02-john-mccarthy.jpg"}
]

# Define the endpoint to list all stickers
@app.get("/figurinhas")
def listar_figurinhas():
    # Return the predefined list of stickers
    return figurinhas
