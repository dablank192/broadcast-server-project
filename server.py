import asyncio
import websockets
import json


connected_user = {}


async def broadcast(msg_dict, exclude_websocket = None): #SEND MSG TO ALL USERS FUNC
    msg_json = json.dumps(msg_dict) #json -> python dict

    receiver = [client for client in connected_user if client != exclude_websocket]

    if receiver:
        await asyncio.gather(*[client.send(msg_json) for client in receiver])


async def handler(websocket): #AUTO RUN WHEN A USER CONNECT TO THE SERVER
    connected_user[websocket] = "Annonymous"

    try:
        async for message in websocket:
            data = json.loads(message) #python dict -> json

            if data["type"] == "set_name":
                old_name = connected_user[websocket]
                new_name = data["username"]
                connected_user[websocket] = new_name

                print(f"User {old_name} change their name to {new_name}")
                await broadcast({"type": "system", "message": f"User {old_name} change their name to {new_name}"})
            
            elif data["type"] == "chat":
                sender_name = connected_user[websocket]
                chat_msg = data["message"]

                print(f"{sender_name} send: {chat_msg}")
                await broadcast({"type": "chat", "sender": sender_name, "message": chat_msg}, exclude_websocket= websocket)
    
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Error {e} has occured")
        await broadcast({"type": "system", "message": f"Error {e} has occured"})

    finally:
        left_user = connected_user.pop(websocket, "Annonymous")

        print(f"User [{left_user}] has disconnected")
        await broadcast({"type": "system", "message": f"User [{left_user}] has left the chat"})


async def main():
    server = await websockets.serve(handler, "localhost", 8000)
    print("Server is running at port: 8000")

    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())