# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request
import os
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask by Insper DS!'

@app.route('/core')
def core():
    return 'Vai Corinthians!!'

@app.route('/add/<a>/<b>')
def add(a, b):
    return str(float(a) + float(b))

@app.route('/area')
def myarea():
  altura = request.args.get('altura', default = 0, type = float)
  largura = request.args.get('largura', default = 0, type = float)
  comprimento = request.args.get('comprimento', default = -1, type = float)
  
  if (comprimento < 0):
        return str(altura*largura)
  else:
        return str(altura*largura*comprimento)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
