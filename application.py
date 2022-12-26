from flask import Flask
app = Flask(__name__)#test-app-0001
@app.route('/')
def hello():
    return 'Hello World!\n'