from flask import Flask, render_template
HTML = ""
with open("templates/day-8.html", "r", encoding="UTF-8") as file:
    HTML = file.read()

app = Flask(__name__)

@app.route("/")
def hello():
    return HTML

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)