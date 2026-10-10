# Voice_Link - V1.0.1

A lightweight real-time voice and text communication prototype built with FastAPI and WebSockets. This project allows multiple browser clients to connect to a central server, send text messages to each other, and use browser-based speech recognition and speech synthesis for voice communication.

## Overview

Voice_Link is designed around a simple server-client model:

- A FastAPI WebSocket server manages client connections
- Each client connects with an ID such as `ASAD` or `LEO`
- Clients can send text messages or voice-transcribed messages to another connected client
- Incoming voice messages are spoken aloud on the receiving browser using the browser's text-to-speech capabilities

```text
ASAD ──► WebSocket Server ──► LEO
LEO ──► WebSocket Server ──► ASAD
```
## Features
- Real-time message relay between connected clients
- WebSocket-based communication
- Text chat support
- Voice input using browser Speech Recognition API
- Audio playback of received voice messages using Speech Synthesis API
- Simple front-end interface served directly from the FastAPI app

## Project Structure
```
Voice_Link/
├── architecture
├── README.md
└── server/
    ├── client.html
    ├── main.py
    └── requirements.txt
```

## Tech Stack
- Python
- FastAPI
- Uvicorn
- WebSockets
- HTML/CSS/JavaScript

## Prerequisites
Before running the project, make sure you have:

- Python 3.9+
- pip
- A modern browser with Web Speech API support (Chrome is recommended)
## Installation
Clone the repository:
``` bash
git clone https://github.com/Asad-In-Data/Voice_Link.git
cd Voice_Link
```
Navigate to the server folder and install dependencies:
``` bash
cd server
pip install -r requirements.txt
```
Run the Application
Start the FastAPI server:
``` bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
Then open the app in your browser:
```
http://localhost:8000
```
## How to Use
- Open the app in two browser tabs or on two devices.
- In each tab, enter a client ID such as ASAD and LEO.
- Click Connect.
- Enter the recipient's ID in the Send to field.
- Send either:
  1. a normal text message, or
  2. a voice message using the Speak button.
## Server Behavior
The backend in server/main.py does the following:

- Accepts WebSocket connections at /ws/{client_id}
- Stores active clients in memory
- Receives JSON payloads from a sender
- Redirects messages to the specified receiver if connected
- Returns an error message if the target user is not online
## Example Message Format
The client sends JSON messages in this format:

``` JSON
{
  "from": "ASAD",
  "to": "LEO",
  "type": "message",
  "data": "Hello LEO"
}
```
For voice messages:

``` JSON
{
  "from": "ASAD",
  "to": "LEO",
  "type": "voice",
  "data": "Hello, can you hear me?"
}
```
## Notes
This project is a simple prototype and does not include user authentication or persistent storage.
The system keeps clients in memory only while the server is running.
Voice features depend on browser support and microphone permissions.
## License
This project is currently provided as-is for educational and demonstration purposes.

## Author
Voice_Link is a personal prototype built for real-time browser-based communication experiments.
