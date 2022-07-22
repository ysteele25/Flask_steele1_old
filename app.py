from flask import Flask, render_template
from flask_navigation import Navigation


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/privacypolicy.html")
def privacypolicy():
    return render_template('privacypolicy.html')


if __name__ == "__main__":
    app.run(debug=True) 