from flask import Flask
app = Flask(__name__)

print "hello world!"

##creating the test app route
@app.route('/')
def hello_world():
    return 'Hello, World!'