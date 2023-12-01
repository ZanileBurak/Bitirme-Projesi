from flask import Flask, render_template, request,redirect, url_for, session

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "super secret key"

from login import login


@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == "POST":
        if login(request.form["userid"],request.form["password"]):
            return redirect('/main')
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")
    
@app.route("/main", methods=['GET', 'POST'])
def mainpage():
    return render_template('main.html')
