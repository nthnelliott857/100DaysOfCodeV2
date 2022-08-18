from flask import Flask, jsonify, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

API_KEY = "TopSecretAPIKey"

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    all_cafes = db.session.query(Cafe).all()
    for cafe in all_cafes:
        print(cafe.name)
        print(cafe.coffee_price)
    return render_template("index.html")


@app.route("/random", methods=["GET", "POST"])
def random_route():
    if request.method == "GET":
        return jsonify(random_cafe=Cafe.query.get(random.randint(a=1, b=21)).name)
        # print(random_cafe.name)
    # return render_template("")

@app.route("/all", methods=["GET", "POST"])
def all():
    if request.method == "GET":
        all_cafes_query = db.session.query(Cafe).all()
        all_cafes = {}
        for cafe in all_cafes_query:
            all_cafes[cafe.id] = cafe.name
        return jsonify(all_cafes)
        # print(all_cafes)





# http://127.0.0.1:5000/search?loc=Peckham
## HTTP GET - Read Record
@app.route("/search", methods=["GET", "POST"])
def search():
    location = request.args.get("loc")
    print(location)

    cafe = Cafe.query.filter_by(location=location).first()
    if cafe is not None:
        cafe = cafe.__dict__
        cafe.pop('_sa_instance_state') # '_sa_instance_state' is not serializable,
                                 # and will produce an error
        return jsonify(cafe=cafe)
    else:
        error = {
            "Not Found": "Sorry, we don't have a cafe at that location."
        }
        return jsonify(error=error)
    # return jsonify(cafe=cafe)
    # print(cafe_match)
## HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        if Cafe.query.filter_by(location=request.form["name"]).first() is None:

            new_cafe = Cafe(
                name=request.form["name"],
                map_url=request.form["map_url"],
                img_url=request.form["img_url"],
                location=request.form["location"],
                seats = request.form["has_sockets"],
                has_toilet = get_boolean_value(request.form["has_toilet"]),
                has_wifi = get_boolean_value(request.form["has_wifi"]),
                has_sockets = get_boolean_value(request.form["can_take_calls"]),
                can_take_calls = get_boolean_value(request.form["seats"]),
                coffee_price = request.form["coffee_price"]
            )
            db.session.add(new_cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully added the new cafe."})

        # print(request.form["name"])
        # print(request.form["map_url"])

def get_boolean_value(value):
    value = int(value)
    return value == 1
## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["GET","PATCH"])
def update_price(cafe_id):
    if request.method == "PATCH":
        # print(request.args.get("new_price"))
        cafe_to_update = Cafe.query.get(cafe_id)
        if cafe_to_update is not None:
            print(cafe_to_update.coffee_price)
            cafe_to_update.coffee_price = request.args.get("new_price")
            print(cafe_to_update.coffee_price)
            db.session.commit()
            all_cafes = db.session.query(Cafe).all()
            return jsonify(response={"success": "Successfully updated the price."})
        else:
            return jsonify(response={"Not Found": "Sorry a cafe with that id was not found in the database."})
## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["GET","PATCH", "DELETE"])
def delete(cafe_id):
    if request.method == "DELETE":
        if request.args.get("api-key") == API_KEY:
            cafe_to_delete = Cafe.query.get(cafe_id)
            if cafe_to_delete is not None:
                db.session.delete(cafe_to_delete)
                db.session.commit()
                all_cafes = db.session.query(Cafe).all()
                return jsonify(response={"success":
                                         "Successfully deleted the cafe."})
            else:
                return jsonify(response={"error":
                                         "Sorry, a cafe with that id was not found in the database."})
        else:
            return jsonify(response={"error":
                                     "Sorry, that's not allowed. Make sure you have the correct api_key"})



if __name__ == '__main__':
    app.run(debug=True)
