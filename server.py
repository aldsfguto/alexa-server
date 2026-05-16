from flask import Flask, jsonify

app = Flask(__name__)

last_command = ""

@app.route("/")
def home():
    return "Servidor online"

@app.route("/send/<cmd>")
def send(cmd):
    global last_command
    last_command = cmd
    return jsonify({"status": "ok", "command": cmd})

@app.route("/get")
def get():
    global last_command
    cmd = last_command
    last_command = ""
    return jsonify({"command": cmd})
