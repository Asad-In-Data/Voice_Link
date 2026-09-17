# Client A ──► Server ──► Client B
# Client B ──► Server ──► Client A

# from http import clients

from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse

clients = {}
app = FastAPI()

@app.get("/")
def home():
    return FileResponse("server\client.html")

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket,client_id:str):
    await websocket.accept()
    clients[client_id] = websocket
    print(f"Client {client_id} connected")
    # print(f"Total Clients Connected:{len(clients)}")
    print(f"Connected clients: {list(clients.keys())}")
    
    try:
        while True:
         message = await websocket.receive_text()
         print(f"{client_id}: {message}")

         for other_id, client in clients.items():

                if other_id != client_id:
                    await client.send_text(
                        f"{client_id}: {message}"
                    )  
    except:

        if client_id in clients:
            del clients[client_id]

        print(f"{client_id} disconnected")
         



