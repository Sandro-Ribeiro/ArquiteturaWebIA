from fastapi import FastAPI

# Initialize the FastAPI application instance
app = FastAPI()

# Define the root endpoint that responds to HTTP GET requests
@app.get("/")
def hello_world():
    # Return a JSON response with a welcome message
    return {"mensagem": "Olá, mundo! 🌍"}

