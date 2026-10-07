import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)
DATA_DIR = "/app/data"
LOG_FILE = os.path.join(DATA_DIR, "app.log")

@app.route("/")
def index():
    os.makedirs(DATA_DIR, exist_ok=True)
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{now_str}: Hello, Docker!\n")
    
    with open(LOG_FILE, "r") as f:
        logs = f.read()

    return f"<p>Hello, Docker!</p><h4>Log:</h4><pre>{logs}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
