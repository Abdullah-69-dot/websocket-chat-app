import asyncio
import json
from websockets.server import serve

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    print(" Client connected")

    try:
        async for message in websocket:
            data = json.loads(message)
            name = data.get("name", "Unknown")
            text = data.get("text", "")
            print(f"💬 {name}: {text}")

            # إرسال الرسالة إلى جميع العملاء المتصلين
            to_remove = []
            for client in connected_clients:
                if client.closed:  # لو الاتصال اتقفل
                    to_remove.append(client)
                    continue
                await client.send(json.dumps({
                    "name": name,
                    "text": text
                }))

            # إزالة العملاء المغلقين
            for client in to_remove:
                connected_clients.remove(client)

    except Exception as e:
        print(f" Error: {e}")

    finally:
        connected_clients.remove(websocket)
        print(" Client disconnected")


async def main():
    async with serve(handler, "localhost", 8080):
        print(" WebSocket server running on ws://localhost:8080")
        await asyncio.Future()  # يبقي السيرفر شغال إلى أجل غير مسمى


if __name__ == "__main__":
    asyncio.run(main())
