from flask import Flask, request, redirect, render_template
import cgi

form = cgi.FieldStorage()

app = Flask(__name__)

@app.route('/bank', methods=['GET', 'POST'])
def message():
   if request.method == "GET":
       return render_template("kalkulator.html")
   elif request.method == "POST":
       pay = request.form["pay"]
       waluta = request.form["Waluta"]
       lolek = (int(float(pay))) / (int(float(waluta)))
       print(request.form, lolek)
       return redirect("/bank")