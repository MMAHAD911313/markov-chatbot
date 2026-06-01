# Markov Chatbot

A simple Python Markov chain chatbot that learns word transitions from training text and generates short responses using random next-word selection.

## Features

- First-order Markov chain text generation
- Simple training from plain text
- Interactive chat loop using console input

## Files

- `markov-chatbot.py` - main chatbot implementation
- `README.md` - project documentation
- `LICENSE` - open source license
- `.gitignore` - files to ignore in version control
- `requirements.txt` - Python dependencies

## Requirements

- Python 3.x

## Usage

```bash
python markov-chatbot.py
```

Then type messages at the prompt. The bot uses the first word of your input as the starting point and generates a response of up to 12 words.

## How it works

1. The bot trains on the sample text inside `markov-chatbot.py`.
2. It builds a dictionary mapping each word to possible following words.
3. During generation, it starts from a word and randomly chooses one of its learned successors repeatedly.

## Custom training data

To improve the bot, replace or expand the text in the `data` variable inside `markov-chatbot.py`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
