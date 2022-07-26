from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def cek():
    return "Web App with Python Flask!"

app.run(host='0.0.0.0', port=8080)
