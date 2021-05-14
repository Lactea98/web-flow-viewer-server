from flask import Flask, render_template, request
from flask_socketio import SocketIO
from tools import *

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
    
    url_info = getParsedUrl(req_header)
    referer_info = getParsedRefererUrl(req_header)
    state_info = getStateCode(res_header)
    mime_info = getMimeType(res_header)


    socketio.emit("receive", {
        "req_header" : req_header, 
        "res_header" : res_header, 
        "url_info" : url_info,
        "state_info" : state_info,
        "mime_info" : mime_info,
        "referer_info" : referer_info
    })
    return "success"

if __name__ == '__main__':
    socketio.run(app, debug=True)