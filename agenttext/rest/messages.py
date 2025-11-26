"""Messages resource"""

from typing import Optional, Dict, Any, List, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from agenttext.rest.agenttext import AgentText


class Messages:
    """Messages resource"""
    
    def __init__(self, client: "AgentText"):
        self._client = client
    
    def send(self, to: str, content: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
        """Send a message"""
        return self._client._request("POST", "/send", json={"to": to, "content": content})
    
    def send_file(self, to: str, file_path: str, text: Optional[str] = None) -> Dict[str, Any]:
        """Send a file"""
        data = {"to": to, "filePath": file_path}
        if text:
            data["text"] = text
        return self._client._request("POST", "/send/file", json=data)
    
    def send_files(self, to: str, file_paths: List[str], text: Optional[str] = None) -> Dict[str, Any]:
        """Send multiple files"""
        data = {"to": to, "filePaths": file_paths}
        if text:
            data["text"] = text
        return self._client._request("POST", "/send/files", json=data)
    
    def send_batch(self, messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Send multiple messages"""
        return self._client._request("POST", "/send/batch", json={"messages": messages})
    
    def list(self, sender: Optional[str] = None, unread_only: Optional[bool] = None,
             limit: Optional[int] = None, since: Optional[str] = None,
             search: Optional[str] = None, has_attachments: Optional[bool] = None,
             exclude_own_messages: Optional[bool] = None) -> Dict[str, Any]:
        """Query messages"""
        params = {}
        if sender:
            params["sender"] = sender
        if unread_only is not None:
            params["unreadOnly"] = str(unread_only).lower()
        if limit is not None:
            params["limit"] = limit
        if since:
            params["since"] = since
        if search:
            params["search"] = search
        if has_attachments is not None:
            params["hasAttachments"] = str(has_attachments).lower()
        # IMPORTANT: Always include excludeOwnMessages if explicitly set
        # The API defaults to true, so we must explicitly pass false
        if exclude_own_messages is not None:
            params["excludeOwnMessages"] = str(exclude_own_messages).lower()
        return self._client._request("GET", "/messages", params=params)
    
    def get_unread(self) -> Dict[str, Any]:
        """Get unread messages"""
        return self._client._request("GET", "/messages/unread")

