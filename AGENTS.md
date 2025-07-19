# AGENTS Instructions

This repository implements a Microsoft Teams bot in **Python**. The bot's goal is to add fun to the development process by detecting messages that match the 5-7-5 syllable pattern of a Haiku or that have the same length as an existing Haiku. When such a message is found, it will respond by reformatting the text as a Haiku.

## Coding guidelines

- Use **Python 3.8+**.
- Follow **PEP8** style. Use black for formatting and flake8 for linting.
- Organize source code under a `haiku_bot` package.
- Include unit tests with **pytest** under `tests/`.
- Document public functions with docstrings.

## Development workflow

## Haiku detection guidelines
- A haiku has a 5–7–5 syllable structure (17 syllables total).
- A message is considered haiku-sized if it has exactly 17 syllables. Approximating syllables with a library such as `textstat` is acceptable.
- When a message qualifies, break it into three lines: 5 syllables, 7 syllables, 5 syllables. The split can be approximate based on word boundaries.

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run linting and tests before committing:
   ```bash
   black haiku_bot
   flake8 haiku_bot
   pytest
   ```
3. Keep README and this file updated with important notes about the bot.

