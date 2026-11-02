# Multiple-Ai

A project that combines multiple chatbots ( gemini, chatgpt, ... ) in one desktop app using their APIs and python.

Right now only gemini works, chat-gpt is coming soon.

## Setup

```bash
git clone https://github.com/I3mk132/Multiple-Ai.git
cd Multiple-Ai
python -m venv venv
source venv/bin/activate
pip install customtkinter google-generativeai python-dotenv
```

On windows activate it with `venv\Scripts\activate`.

You can use `pip install -r requirements.txt` instead, but it needs python 3.13 or older.

Then make a `.env` file in the main folder and put your [gemini key](https://aistudio.google.com/apikey) in it:

```
GEMINI_API_KEY=your_key
```

## Run

```bash
python main.py
```

## How to use

1. Choose `new` for a new chat or `old` to continue a saved one
2. Choose `gemini`
3. Press the ✓ on the top
4. Write your message and press Enter or the ✓ next to the box

`Shift+Enter` makes a new line and `Ctrl+Backspace` clears the box.

Chats are saved as json files in `multipleAi/saved_chats`.

## Files

- `main.py` starts the app
- `multipleAi/gui.py` the window and the buttons
- `multipleAi/gemini.py` talks to gemini and saves the chats
- `multipleAi/cAI.py` a separate test for character ai, it needs `characterai` installed and `CAI_TOKEN` in the `.env`
- `multipleAi/complex.drawio` diagram of how the functions connect
- `multipleAi/files_for_later` old gui and a fonts tool

## Things to fix

- Add chat-gpt
- The window freezes until the answer comes
- Move from `google-generativeai` to `google-genai` because the old one is not supported anymore
