# Client A ──► Server ──► Client B
# Client B ──► Server ──► Client A

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hiiiiiiii!"}


