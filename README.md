# Broadcast Server (WebSocket)

This project is a real-time Broadcast Server from [roadmap.sh Broadcast Server Project](https://roadmap.sh/projects/broadcast-server).

The application allows multiple clients to connect concurrently, set custom usernames, and exchange messages. Any message sent to the server is immediately broadcast to all other online users in the room.

## 🚀 Features

* **Real-time Communication:** Bi-directional, low-latency communication utilizing the WebSocket protocol.

* **Broadcast Mechanism:** Automatically routes incoming messages to all connected clients (excluding the original sender).

* **Username Customization:** Users can identify themselves by setting and updating their display names dynamically.

* **System Notifications:** Automated room-wide alerts for events such as new user joins, name changes, and disconnections.

* **JSON Payload:** All client-server communication is structured and parsed using standard JSON formats.

## 🛠️ Tech Stack

* **Backend:** Python (utilizing the built-in `asyncio` library for asynchronous I/O and the `websockets` package).

* **Frontend:** Vanilla HTML and JavaScript (leveraging the browser's native WebSocket API, no external frameworks required).

## ⚙️ Installation

1. Ensure you have Python installed on your machine (version 3.7 or higher is recommended).

2. Install the required `websockets` package using `pip`:

```bash
pip install websockets

## 🏃 Getting Started

* Step 1: Start the Server

Open your terminal or command prompt, navigate to the project directory, and run the server script:

python server.py


If successful, you should see the message: 🚀 Server is running on port 8000...

* Step 2: Connect the Clients

This project does not require a complex web server setup for the frontend.

Open the index.html file directly in any modern web browser (Chrome, Edge, Firefox, etc.).

To simulate a multi-user environment, open the index.html file in 2 or 3 separate browser tabs.

Enter a username, click "Đổi Tên" (Change Name), and start chatting!

## 📂 Project Structure

server.py: Contains the core asynchronous logic for the WebSocket Server.

index.html: A lightweight, responsive UI and client-side JavaScript to interact with the server.