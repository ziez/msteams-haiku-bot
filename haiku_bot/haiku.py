"""Utility functions for detecting and formatting haiku messages."""

from typing import List


def is_haiku_size(message: str) -> bool:
    """Return True if the message is exactly 17 characters ignoring spaces."""
    compact = message.replace(" ", "")
    return len(compact) == 17


def to_haiku(message: str) -> List[str]:
    """Split a 17-character message into 5-7-5 lines.

    If the message isn't haiku sized, return the original text as a single
    item list.
    """
    if not is_haiku_size(message):
        return [message]
    compact = message.replace(" ", "")
    return [compact[:5], compact[5:12], compact[12:17]]
