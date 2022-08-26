"""
#REMINDERS
1. The data we access will be instance(s) of objects and require dot notation to target informaiton and methods.

#TO-DO:
1. Update the object name in the import statement
2. Generate necessary routes
"""

from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
            
@app.route('/edit/<int:id>')
def show(id):
    ninjas = Ninja.get_all()
    for ninja in ninjas:
        if ninja.id == id:
            selected_ninja = ninja
    print(selected_ninja)
    return render_template("ninja_edit.html", ninja = selected_ninja)

@app.route("/update_user/<int:id>" methods=["POST"])
def update(id):
    ninjas = Ninja.get_all()
    for ninja in ninjas:
        if ninja.id == id:
    return redirect("")


# @app.route('/NAME-ROUTE', methods=["POST"])
# def create():
#     data = {
#         "first_name": request.form["first_name"],
#         "last_name" : request.form["last_name"],
#         "email": request.form["email"]
#     }
#     User.save(data)
#     return redirect('/NAME-ROUTE')
