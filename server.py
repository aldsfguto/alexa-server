from flask import Flask, jsonify
from wakeonlan import send_magic_packet

app = Flask(__name__)

# MAC ADDRESS DO SEU PC
MAC = "22:23:5C:04:00:D8"

# GUARDA O ÚLTIMO COMANDO
last_command = ""

# HOME
@app.route("/")
def home():
    return "Servidor online"

# LIGAR PC VIA WAKE ON LAN
@app.route("/ligar")
def ligar():
    send_magic_packet(MAC)

    return jsonify({
        "status": "ok",
        "message": "Pacote Wake-on-LAN enviado"
    })

# ENVIAR COMANDO
@app.route("/send/<cmd>")
def send(cmd):
    global last_command

    last_command = cmd

    return jsonify({
        "status": "ok",
        "command": cmd
    })

# AGENTE DO PC BUSCA COMANDOS
@app.route("/get")
def get():
    global last_command

    cmd = last_command
    last_command = ""

    return jsonify({
        "command": cmd
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
