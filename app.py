from flask import *
import magic
import csci462

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=["POST"])
def encrypt():
    f = request.files['data']
    f.save('input.dat')
    m = open('input.dat').read()
    t = request.form.get('password')
    print 'Password: {}'.format(t)
    x = csci462.enc(m, t)
    f = open('output.enc', 'wb')
    f.write(''.join([chr(c) for c in x]))
    f.close()
    return send_file('output.enc', as_attachment=True)

@app.route('/decrypt', methods=["POST"])
def decrypt():
    f = request.files['data']
    f.save('input.dat')
    c = open('input.dat').read()
    t = request.form.get('password')
    print 'Password: {}'.format(t)
    x = csci462.dec(c, t)
    f = open('output.dat', 'wb')
    f.write(''.join([chr(y) for y in x]))
    f.close()
    return send_file('output.dat', as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1337)