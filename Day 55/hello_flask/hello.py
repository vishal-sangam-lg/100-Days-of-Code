from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<div style="height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: ' \
           'center">' \
           '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img height="300" src="https://wallpapercave.com/dwp2x/wp11742613.jpg"></img>' \
           '</div>'


@app.route("/bye")
def bye():
    return 'Bye'


# Try this url to understand - http://127.0.0.1:5000/username/Vishal/2/test
@app.route("/username/<name>/<int:number>/<path:anything>")
def greeting(name, number, anything):
    return f"Hello there, {name}!, number is {number}, anything: {anything}"


if __name__ == "__main__":
    app.run(debug=True)
