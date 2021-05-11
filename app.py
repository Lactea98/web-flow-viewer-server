from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
socketio = SocketIO(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route("/log", methods=["POST"])
def log():
    req_header = request.form["request_header"]
    res_header = request.form["response_header"]
    socketio.emit("receive", {'req_header' : req_header, 'res_header' : res_header})

    return "success"



if __name__ == '__main__':
    socketio.run(app, debug=True)