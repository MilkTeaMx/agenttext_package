# AgentText Python SDK

Python client library for the AgentText iMessage REST API.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd agenttext-python
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the package:**
   ```bash
   pip install -e .
   ```

4. If you are working in a different project or a separate virtual environment, you can install the SDK directly from its folder by passing the full path:

pip install -e /path/to/agenttext-python


## Usage

```python
from agenttext import AgentText

# Initialize client (API server must be running on http://localhost:3000)
client = AgentText()

# Send a message
result = client.messages.send(to="+1234567890", content="Hello!")

# Get unread messages
unread = client.messages.get_unread()
print(f"Unread: {unread['total']} messages")

# List chats
chats = client.chats.list(limit=10)
for chat in chats:
    print(f"{chat['displayName']}: {chat['unreadCount']} unread")
```

## Prerequisites

- Python 3.7 or higher
- AgentText API server running on `http://localhost:3000`
  - Start it from the `agenttext_api` directory: `npm run api` or `bun run api-server.ts`

## Examples

Run the example script:
```bash
python examples/simple.py
```

## API Reference

### AgentText Client

```python
client = AgentText(base_url="http://localhost:3000", timeout=30)
```

### Messages

- `client.messages.send(to, content)` - Send a message
- `client.messages.send_file(to, file_path, text=None)` - Send a file
- `client.messages.send_files(to, file_paths, text=None)` - Send multiple files
- `client.messages.send_batch(messages)` - Send multiple messages
- `client.messages.list(**filters)` - Query messages
- `client.messages.get_unread()` - Get unread messages

### Chats

- `client.chats.list(**filters)` - List chats

### Watcher

- `client.watcher.start(webhook=None)` - Start message watcher
- `client.watcher.stop()` - Stop watcher
- `client.watcher.status()` - Get watcher status

## Error Handling

```python
from agenttext import AgentText, AgentTextAPIException, AgentTextConnectionException

try:
    result = client.messages.send(to="+1234567890", content="Hello!")
except AgentTextAPIException as e:
    print(f"API Error: {e.status_code} - {e.message}")
except AgentTextConnectionException as e:
    print(f"Connection Error: {e}")
```
