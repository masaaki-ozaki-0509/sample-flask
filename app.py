from flask import Flask
from flask import render_template
app = Flask(__name__)

'''
@app.route('/')
def index():
    hello = 'Hello world!'
    return hello
'''
@app.route('/')
def index():
    hello = 'Hello world!'
    return render_template('index.html', hello=hello)
if __name__ == '__main__':
    app.run(debug=True)


