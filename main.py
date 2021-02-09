from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/index")