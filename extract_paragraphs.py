import os
import cohere
from dotenv import load_dotenv
import time
import sys
import threading

load_dotenv()
api_key = os.getenv('COHERE_API_KEY')

co = cohere.ClientV2(api_key=api_key)

PROMPT_FILE = "prompt.txt"

def show_timer(stop_event):
    start = time.time()
    while not stop_event.is_set():
        elapsed = int(time.time() - start)
        if elapsed < 60:
            time_str = f"{elapsed}s"
        else:
            minutes, seconds = divmod(elapsed, 60)
            time_str = f"{minutes}m{seconds}s"
        sys.stdout.write(f"\rExtracting... Time elapsed: {time_str}")
        sys.stdout.flush()
        time.sleep(0.1)

def clean_text_with_timer(txt_file):
    start_time = time.time()
    stop_event = threading.Event()
    timer_thread = threading.Thread(target=show_timer, args=(stop_event,))
    timer_thread.start()

    clean_text(txt_file)

    stop_event.set()
    timer_thread.join()
    elapsed = int(time.time() - start_time)
    if elapsed < 60:
        print(f"\rExtraction done! Total time: {elapsed}s")
    else:
        minutes, seconds = divmod(elapsed, 60)
        print(f"\rExtraction done! Total time: {minutes}m{seconds}s")

def clean_text(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

    with open(PROMPT_FILE, "r") as file:
        message = file.read() + file_content

    response = co.chat(
        model="command-r-plus-08-2024",
        messages=[{"role": "user", "content": message}]
    )

    corrected_text = response.message.content[0].text

    with open(file_path, 'w') as file:
        file.write(corrected_text)
