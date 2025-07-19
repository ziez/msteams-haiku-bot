"""Utility functions for detecting and formatting haiku messages."""

from typing import List

import textstat


def is_haiku_size(message: str) -> bool:
    """Return ``True`` if the message contains exactly 17 syllables."""
    return textstat.textstat.syllable_count(message) == 17


def to_haiku(message: str) -> List[str]:
    """Split a 17-syllable message into lines of approximately 5-7-5.

    If the message isn't haiku sized, the original text is returned as a
    single-element list.
    """
    if not is_haiku_size(message):
        return [message]

    words = message.split()
    targets = [5, 7, 5]
    lines: List[str] = []
    current_words: List[str] = []
    current_syllables = 0
    target_index = 0

    for word in words:
        syllables = textstat.textstat.syllable_count(word)
        if current_syllables + syllables > targets[target_index]:
            lines.append(" ".join(current_words))
            current_words = [word]
            current_syllables = syllables
            target_index += 1
        else:
            current_words.append(word)
            current_syllables += syllables

    lines.append(" ".join(current_words))
    return lines
