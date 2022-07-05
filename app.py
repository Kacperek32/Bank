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
       lolek = 3.4
       print(request.form, pay)
       lolek2 = lolek / pay
       print(f"{lolek2}")
       return redirect("/bank")