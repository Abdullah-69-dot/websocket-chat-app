# 💬 PushChat - Real-time WebSocket Chat Application

A lightweight, real-time chat application built with Python WebSockets and vanilla JavaScript. Features a clean, modern UI with push-based message delivery.

## ✨ Features

- **Real-time Communication**: Instant message delivery using WebSocket protocol
- **Push Pattern**: Server broadcasts messages to all connected clients
- **Clean UI**: Modern, responsive design with smooth animations
- **Simple Architecture**: Minimal dependencies, easy to understand and extend
- **Multi-client Support**: Multiple users can chat simultaneously

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- `websockets` library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pushchat.git
cd pushchat
```

2. Install dependencies:
```bash
pip install websockets
```

### Running the Application

1. Start the WebSocket server:
```bash
python server.py
```

You should see:
```
🚀 WebSocket server running on ws://localhost:8080
```

2. Open `index.html` in your web browser (you can open multiple tabs to simulate different users)

3. Enter your name and start chatting!

## 📁 Project Structure

```
pushchat/
├── server.py       # Python WebSocket server
├── index.html      # Client-side HTML/CSS/JS
└── README.md       # This file
```

## 🛠️ Technical Details

### Server Side (`server.py`)
- Built with Python's `asyncio` and `websockets` library
- Maintains a set of connected clients
- Broadcasts incoming messages to all connected clients
- Handles client connections and disconnections gracefully
- Automatic cleanup of closed connections

### Client Side (`index.html`)
- Vanilla JavaScript WebSocket client
- Real-time message rendering
- Distinguishes between own messages and others' messages
- Smooth fade-in animations for new messages
- Auto-scroll to latest message

## 🎨 Features Breakdown

### Message Flow
1. User enters name and message
2. Client sends JSON payload to server via WebSocket
3. Server receives message and broadcasts to all connected clients
4. Each client displays the message with appropriate styling

### Message Format
```json
{
  "name": "Username",
  "text": "Message content"
}
```

## 🔧 Customization

### Changing the Port
Edit `server.py`:
```python
async with serve(handler, "localhost", 8080):  # Change 8080 to your port
```

And `index.html`:
```javascript
let ws = new WebSocket("ws://localhost:8080");  // Update port here too
```

### Styling
All styles are contained in the `<style>` section of `index.html`. Customize colors by modifying CSS variables:
```css
:root {
  --blue: #2563eb;
  --light: #f1f5f9;
  --white: #ffffff;
  --gray: #d1d5db;
  --text: #1f2937;
}
```

## 🌐 Deployment Notes

For production deployment:
- Replace `localhost` with your server's IP/domain
- Consider using `wss://` (WebSocket Secure) instead of `ws://`
- Add authentication and validation
- Implement rate limiting
- Add persistent message storage if needed

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Built with ❤️ using Python WebSockets

---

**Happy Chatting! 💬**