from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.dog_model import Dog
# import your models as needed

#  ! *************** RENDER ROUTES ***************
@app.route('/')
def false_start():
    return redirect("/dogs/create")


@app.route("/dogs/create")
def create_dog_page():
    return render_template("create.html")

@app.route("/dogs")
def dashboard():
    all_dogs = Dog.get_all()
    return render_template("dashboard.html", dogs = all_dogs)

@app.route("/dogs/update/<int:id>")
def update_dog_page(id):
    dog = Dog.get_one({"id" : id})
    print(dog)
    return render_template("edit.html", dog = dog)



# ! **************POST ROUTES ***************

@app.route("/dogs/save", methods=["POST"])
def save_dog():
    dog_data = {
        **request.form
    }
    Dog.create(dog_data)
    return redirect("/dogs")

@app.route("/dogs/update/<int:id>", methods = ["POST"])
def update_dog(id):
    data = {
        "id" : id,
        **request.form
    }
    Dog.update(data)
    return redirect("/dogs")