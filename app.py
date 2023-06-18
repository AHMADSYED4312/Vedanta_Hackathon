from flask import Flask,render_template, redirect, request

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route('/login',methods=["GET","POST"])
def login():
    return render_template("signin.html")


if __name__ == "__main__":
    app.run()