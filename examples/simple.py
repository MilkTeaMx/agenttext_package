#!/usr/bin/env python3
"""Simple example"""

from agenttext import AgentText

client = AgentText()

# Health check
health = client.health()
print(f"API Status: {health['status']}")

# Get unread messages
unread = client.messages.get_unread()
print(f"Unread: {unread['total']} messages from {unread['senderCount']} senders")

# List chats
chats = client.chats.list(limit=5)
print(f"\nRecent chats:")
for chat in chats:
    print(f"  - {chat['displayName']} ({chat['unreadCount']} unread)")

