"""MS Teams Haiku Bot package."""

__all__ = ["is_haiku_size", "to_haiku", "handle_message"]

from .haiku import is_haiku_size, to_haiku
from .bot import handle_message
