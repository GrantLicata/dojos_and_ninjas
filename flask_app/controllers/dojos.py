"""
#REMINDERS
1. The data we access will be instance(s) of objects and require dot notation to target informaiton and methods.

#TO-DO:
1. Update the object name in the import statement
2. Generate necessary routes
"""

from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojo_create.html", dojos = dojos)

@app.route('/create_dojo', methods=["POST"])
def create():
    data = {
        "name": request.form["name"]
    }
    if len(data["name"]) > 1:
        Dojo.save(data)
    else:
        print("Dojo name is too short.")
    return redirect("/")

@app.route("/dojo_details/<int:id>")
def details(id):
    dojos = Dojo.get_all()
    ninjas = Ninja.get_all()

    for dojo in dojos:
        if dojo.id == id:
            print(dojo.id)
            print(dojo.name)
            selected_dojo = dojo

    dojo_ninjas = []
    for ninja in ninjas:
        if ninja.dojo == id:
            dojo_ninjas.append(ninja)
            print(ninja)

            

    return render_template("dojo_details.html", id = id, dojo = selected_dojo, ninjas = dojo_ninjas)