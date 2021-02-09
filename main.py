from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/parent', methods=['GET'])
def contact():
    return render_template("contact.html")
