"""Entry point for the MS Teams Haiku bot."""

from .haiku import is_haiku_size, to_haiku


def handle_message(message: str) -> str:
    """Process a message and return a haiku if appropriate."""
    if is_haiku_size(message):
        return "\n".join(to_haiku(message))
    return message


# Placeholder for future Teams integration
if __name__ == "__main__":
    import sys

    incoming = " ".join(sys.argv[1:])
    print(handle_message(incoming))
