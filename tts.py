import os
import pyttsx3

def narrate_text(input_file):
    if os.path.exists(input_file):
        engine = pyttsx3.init()
        engine.setProperty('rate', 175)
        engine.setProperty('volume', 0.5)

        with open(input_file, "r") as f:
            content = f.read()
            engine.say(content)
            engine.runAndWait()
            engine.stop()
    else:
        print(f"The file '{input_file}' does not exist. Please check the file path.")
