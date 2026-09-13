from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Flask activo</h1><p>Servidor local en 127.0.0.1:5000</p>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
