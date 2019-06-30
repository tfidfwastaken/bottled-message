from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", message="Message Appears Here")

@app.route("/submit", methods=["POST"])
def submit():
    confirmed = True
    text = request.form.get("bottletext")
    if text == "":
        confirmed = False
    return render_template("index.html", confirmed=confirmed)

@app.route("/retrieve")
def retrieve():
    message="ayo"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
