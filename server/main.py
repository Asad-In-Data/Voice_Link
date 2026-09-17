# Client A ──► Server ──► Client B
# Client B ──► Server ──► Client A

# from http import clients

from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse

clients = []
app = FastAPI()

@app.get("/")
def home():
    return FileResponse("server\client.html")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    print(f"Total Clients Connected:{len(clients)}")
    
    try:
        while True:
         message = await websocket.receive_text()
         print(f"Recived message: {message}")
         for client in clients:
            if client != websocket:
                await client.send_text(message)
                
                
    except :
        clients.remove(websocket)
        print(f"Total Clients Connected:{len(clients)}")
         



