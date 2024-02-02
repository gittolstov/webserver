from flask import Flask, render_template, request
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


@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        for item in request.form:
            print(item, request.form[item])
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
