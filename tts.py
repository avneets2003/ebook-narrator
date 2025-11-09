import os
import pyttsx3
import threading
import time
import re

pause_flag = False
stop_flag = False
current_index = 0

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def monitor_input():
    global pause_flag, stop_flag
    while True:
        if pause_flag:
            command = input(f"Enter {GREEN}:r{RESET} to resume and {RED}:q{RESET} to quit\n").strip()
        else:
            command = input(f"Enter {YELLOW}:p{RESET} to pause and {RED}:q{RESET} to quit\n").strip()
        if command == ":p":
            print("Narration paused.")
            pause_flag = True
        elif command == ":r":
            print("Narration resumed.")
            pause_flag = False
        elif command == ":q":
            print("Narration stopped.")
            stop_flag = True
            break

def setup_tts_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 0.5)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[132].id)
    return engine

def split_into_sentences(text):
    return re.split(r'(?<=[.!?]) +', text)

def narrate_text(input_file):
    global pause_flag, stop_flag, current_index

    if not os.path.exists(input_file):
        print(f"The file '{input_file}' does not exist. Please check the file path.")
        return

    with open(input_file, "r") as f:
        full_text = f.read()

    sentences = split_into_sentences(full_text)
    engine = setup_tts_engine()

    input_thread = threading.Thread(target=monitor_input, daemon=True)
    input_thread.start()

    while current_index < len(sentences):
        if stop_flag:
            break

        if pause_flag:
            engine.stop()
            time.sleep(0.1)
            continue

        sentence = sentences[current_index]
        engine.say(sentence)
        engine.runAndWait()
        current_index += 1

    engine.stop()
    print("Narration ended.")
