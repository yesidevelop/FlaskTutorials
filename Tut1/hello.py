from flask import Flask, request, redirect
app = Flask(__name__)

@app.route("/")
def Hello():
    return "Hello World"
    

@app.route('/user/<name>')
def user(name):
    return "Hello. This user has name: {}".format(name)

@app.route('/request')
def req():
    return "Request Header is: {}".format(request.headers.get('User-Agent'))

@app.route('/bad')
def bad():
    return "This is bad request", 400

@app.route('/redirect')
def redct():
    return redirect("https://www.google.com")