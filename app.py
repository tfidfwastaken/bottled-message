from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    text = request.form.get("bottletext")
    return text

if __name__ == "__main__":
    app.run(debug=True)
