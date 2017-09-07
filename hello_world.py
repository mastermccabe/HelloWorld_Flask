from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello_world():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('helloworld.html')

@app.route('/hello')
def hello():
    return "hello, World"
    

app.run(debug=True)
