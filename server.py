from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form.get('username')
    return f"Hello, {username}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
