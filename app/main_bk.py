from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "赤城加賀蒼龍飛龍翔鶴瑞鶴大鳳天城葛城"
