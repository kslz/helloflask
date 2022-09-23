from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'


@app.route('/greet/')
@app.route('/greet/<name>')
def greet(name='Programmer'):
    return '<h1>Hello, %s!</h1>' % name

#
# if __name__ == '__main__':
#     app.config.update(DEBUG=True)
#     app.run(host="0.0.0.0", port=9000)
