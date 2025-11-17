"""Exception classes"""

class AgentTextException(Exception):
    """Base exception"""
    pass

class AgentTextAPIException(AgentTextException):
    """API error"""
    def __init__(self, status_code: int, error_type: str, message: str):
        self.status_code = status_code
        self.error_type = error_type
        self.message = message
        super().__init__(f"API Error ({status_code}): {error_type} - {message}")

class AgentTextConnectionException(AgentTextException):
    """Connection error"""
    pass

