from flask import Flask
from wakeonlan import send_magic_packet

app = Flask(__name__)

MAC = "22-23-5C-04-00-D8"

@app.route("/")
def home():
    return "Servidor online"

@app.route("/ligar")
def ligar():
    send_magic_packet(MAC)
    return "Pacote enviado"
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
