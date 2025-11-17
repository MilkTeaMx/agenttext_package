"""Chats resource"""

from typing import Optional, List, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from agenttext.rest.agenttext import AgentText


class Chats:
    """Chats resource"""
    
    def __init__(self, client: "AgentText"):
        self._client = client
    
    def list(self, type: Optional[str] = None, has_unread: Optional[bool] = None,
             sort_by: Optional[str] = None, search: Optional[str] = None,
             limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """List chats"""
        params = {}
        if type:
            params["type"] = type
        if has_unread is not None:
            params["hasUnread"] = has_unread
        if sort_by:
            params["sortBy"] = sort_by
        if search:
            params["search"] = search
        if limit is not None:
            params["limit"] = limit
        return self._client._request("GET", "/chats", params=params)

