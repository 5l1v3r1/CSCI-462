from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=["POST"])
def encrypt():
    pass

@app.route('/decrypt', methods=["POST"])
def decrypt():
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1337)