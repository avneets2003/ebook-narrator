# Text-to-Speech App

## Steps for Installation (Mac)

Ensure that you have Homebrew installed.

1. `brew install espeak ffmpeg ollama`

2. `brew services start ollama`

3. `python -m venv venv`

4. `source venv/bin/activate`

5. `pip install --upgrade pip`

6. `pip install -r requirements.txt`

7. `python app.py`