from flask import Flask, render_template, request
import random

app = Flask(__name__)

messages = []

@app.route("/")
def index():
    return render_template("index.html", message="Message Appears Here")

@app.route("/submit", methods=["POST"])
def submit():
    confirmed = True
    text = request.form.get("bottletext")
    messages.append(text)
    if text == "":
        confirmed = False
    return render_template("index.html", confirmed=confirmed)

@app.route("/retrieve")
def retrieve():
    message = "No messages in the sea :( ...Maybe you can add one?"
    if messages != []:
        message = random.choice(messages)
        messages.remove(message)
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
