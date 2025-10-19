
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
