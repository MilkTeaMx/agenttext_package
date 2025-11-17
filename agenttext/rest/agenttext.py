"""Main AgentText client"""

import requests
from typing import Optional, Dict, Any
from agenttext.exceptions import AgentTextAPIException, AgentTextConnectionException
from agenttext.rest.messages import Messages
from agenttext.rest.chats import Chats
from agenttext.rest.watcher import Watcher


class AgentText:
    """Main client for AgentText REST API"""
    
    def __init__(self, base_url: str = "http://localhost:3000", timeout: Optional[int] = 30):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.messages = Messages(self)
        self.chats = Chats(self)
        self.watcher = Watcher(self)
    
    def _request(self, method: str, endpoint: str, params: Optional[Dict[str, Any]] = None, 
                 json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make HTTP request"""
        url = f"{self.base_url}{endpoint}"
        headers = {"Content-Type": "application/json"}
        
        try:
            response = requests.request(method, url, params=params, json=json, 
                                      headers=headers, timeout=self.timeout)
            
            if not response.ok:
                try:
                    error_data = response.json()
                    error_type = error_data.get("error", "Unknown Error")
                    error_message = error_data.get("message", "No error message")
                except ValueError:
                    error_type = "HTTP Error"
                    error_message = response.text or f"HTTP {response.status_code}"
                
                raise AgentTextAPIException(response.status_code, error_type, error_message)
            
            if response.status_code == 204 or not response.content:
                return {}
            
            return response.json()
        
        except requests.exceptions.RequestException as e:
            raise AgentTextConnectionException(f"Connection error: {str(e)}") from e
    
    def health(self) -> Dict[str, Any]:
        """Check API health"""
        return self._request("GET", "/health")
    
    def info(self) -> Dict[str, Any]:
        """Get API info"""
        return self._request("GET", "/info")

