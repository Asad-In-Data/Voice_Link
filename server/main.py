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
async def websocket_endpoint(websocket: WebSocket, client_id: str):

    await websocket.accept()

    clients[client_id] = websocket

    print(f"{client_id} connected")
    print(f"Connected clients: {list(clients.keys())}")

    try:

        while True:

            message = await websocket.receive_json()

            sender = message["from"]
            receiver = message["to"]

            print(f"{sender} → {receiver}: {message}")

            if receiver in clients:

                await clients[receiver].send_json(message)

            else:

                await websocket.send_json({
                    "type": "error",
                    "data": f"{receiver} is not connected"
                })

    except:

        if client_id in clients:
            del clients[client_id]

        print(f"{client_id} disconnected")
         



