from flask import Flask
import platform

app = Flask(__name__)

@app.route('/')
def hello_world():
    arch = platform.processor()
    retString = """<h1>Hello, World ! - Pyflask Demo \
                   running on <font color=red>{arch}</font> \
                   hardwarearchitecture</h1>""".format(arch=arch)
    return retString

@app.route('/version')
def get_version():
    return '<h1>App version : <b>1.0</b></h1>'

@app.route('/test')
def get_test():
    return '<h1>You are accessing /test endpoint</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
