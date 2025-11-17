"""Watcher resource"""

from typing import Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from agenttext.rest.agenttext import AgentText


class Watcher:
    """Watcher resource"""
    
    def __init__(self, client: "AgentText"):
        self._client = client
    
    def start(self, webhook: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Start watcher"""
        data = {}
        if webhook:
            data["webhook"] = webhook
        return self._client._request("POST", "/watcher/start", json=data)
    
    def stop(self) -> Dict[str, Any]:
        """Stop watcher"""
        return self._client._request("POST", "/watcher/stop")
    
    def status(self) -> Dict[str, Any]:
        """Get watcher status"""
        return self._client._request("GET", "/watcher/status")

