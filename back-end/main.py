import os
import glob
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI application instance
app = FastAPI()

# Add CORS middleware to allow cross-origin requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define absolute paths to ensure the server finds the folder regardless of where it's executed
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Define the list of stickers with their metadata and image URLs
figurinhas = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "John McCarthy", "categoria": "IA", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Sam", "categoria": "Pioneiros", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Geoffrey", "categoria": "Pioneiros", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Yann", "categoria": "Pioneiros", "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6, "nome": "Guido", "categoria": "Pioneiros", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Tim", "categoria": "Pioneiros", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Ray", "categoria": "Pioneiros", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Travis", "categoria": "Pioneiros", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Wes", "categoria": "Pioneiros", "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Edgar", "categoria": "Pioneiros", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Larry", "categoria": "Pioneiros", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Michael", "categoria": "Pioneiros", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Salvatore", "categoria": "Pioneiros", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Eliot", "categoria": "Pioneiros", "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Linus", "categoria": "Pioneiros", "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Dennis", "categoria": "Pioneiros", "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Richard", "categoria": "Pioneiros", "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Bill", "categoria": "Pioneiros", "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Steve", "categoria": "Pioneiros", "imagem_url": "/figurinhas/20/imagem"},
    {"id": 21, "nome": "Paulo", "categoria": "Alura", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Guilherme", "categoria": "Alura", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Gus", "categoria": "Alura", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Mauricio", "categoria": "Alura", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Andre", "categoria": "Alura", "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Guilherme", "categoria": "Alura", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Gi", "categoria": "Alura", "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Vinicius", "categoria": "Alura", "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Rafa", "categoria": "Alura", "imagem_url": "/figurinhas/29/imagem"},
    {"id": 30, "nome": "Sandro", "categoria": "Alura", "imagem_url": "/figurinhas/30/imagem"},
]

# Define the endpoint to list all stickers
@app.get("/figurinhas")
def listar_figurinhas():
    # Return the predefined list of stickers
    return figurinhas

# Define the endpoint to serve the image for a specific sticker ID
@app.get("/figurinhas/{id}/imagem")
def obter_imagem(id: int):
    # Use glob to find the image file starting with the ID formatted as 2 digits
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)
    
    # If no file is found, return a 404 error
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
        
    # Return the first matched file as a FileResponse
    return FileResponse(arquivos[0])
