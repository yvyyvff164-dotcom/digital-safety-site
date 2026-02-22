from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def python_page():
    return render_template("python.html")

@app.route("/print")
def print_page():
    return render_template("print.html")

@app.route("/variables")
def variables():
    return render_template("variables.html")

@app.route("/conditions")
def conditions():
    return render_template("conditions.html")

@app.route("/functions")
def functions():
    return render_template("functions.html")

@app.route("/sorting")
def sorting():
    return render_template("sorting.html")

@app.route("/arrays1")
def arrays1():
    return render_template("arrays1.html")

@app.route("/arrays2")
def arrays2():
    return render_template("arrays2.html")

@app.route("/add_remove")
def add_remove():
    return render_template("add_remove.html")

# ⚠️ МАҢЫЗДЫ
if __name__ == "__main__":
    app.run()