from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/causes")
def causes():
    return render_template("causes.html")

@app.route("/solutions")
def solutions():
    return render_template("solutions.html")

if __name__ == "__main__":
    app.run(debug=True)
