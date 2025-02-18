from typing import Optional, Set
from pydantic import BaseModel
from enum import Enum


class EntityType(str, Enum):
    USER = "user"
    DEVELOPER = "developer"


class AuthContext(BaseModel):
    """JWT decoded context"""
    user_id: str  # Single identifier for the user
