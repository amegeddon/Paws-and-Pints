import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_pubs")
def get_pubs():
    # Fetch the list of pubs
    pubs_cursor = mongo.db.pubs.find()
    pubs = list(pubs_cursor)
    print("Number of pubs fetched:", len(pubs))

    # For each pub, fetch the reviews and associate them with the pub
    for pub in pubs:
        pub_id_str = str(pub['_id'])  # Convert ObjectId to string
        pub_reviews_cursor = mongo.db.reviews.find({'pub_id': pub_id_str})
        pub_reviews = list(pub_reviews_cursor)
        pub['reviews'] = pub_reviews

    # Pass the list of pubs with associated reviews to the template
    reviews_cursor = mongo.db.reviews.find()
    reviews = list(reviews_cursor)
    print("Number of reviews fetched:", len(reviews))

    return render_template("reviews.html", pubs=pubs, reviews=reviews)




@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                             request.form.get("username").capitalize())) 
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route('/write_review', methods=["GET", "POST"])
def write_review():
    if request.method == "POST":
        
        title = request.form.get('title')
        review_text = request.form.get('review_text')
        user_rating = request.form.get('user_rating')
        pub_id = request.form.get('pub_id')
        
        review_data = {
            "title": title,
            "review_text": review_text,
            "user_rating": user_rating,
            "pub_id": pub_id
        }
        
        mongo.db.reviews.insert_one(review_data)
        
        flash("Review Successfully Added")
        return redirect(url_for("get_pubs"))  
        
    else:
        pub_id = request.args.get('pub_id')
        return render_template("write_review.html", pub_id=pub_id)



@app.route("/add_pub", methods=["GET", "POST"])
def add_pub():
    if request.method == "POST":
        
        pub_name = request.form.get("name")
        pub_location = request.form.get("location")
        pub_description = request.form.get("description")
        # Converts checkbox values to Boolean
        food_served = request.form.get("food_served") == "yes"
        dogs_allowed = request.form.get("dogs_allowed") == "yes"
        water_provided = request.form.get("water_provided") == "yes"
        dog_meals = request.form.get("dog_meals") == "yes"
        nearby_walks = request.form.get("nearby_walks") == "yes"
        loving_staff = request.form.get("loving_staff") == "yes"
        
        # Constructs dictionary
        pub_data = {
            "name": pub_name,
            "location": pub_location,
            "description": pub_description,
            "food_served": food_served,
            "dogs_allowed": dogs_allowed,
            "water_provided": water_provided,
            "dog_meals": dog_meals,
            "nearby_walks": nearby_walks,
            "loving_staff": loving_staff
        }
        
        mongo.db.pubs.insert_one(pub_data)
        
        flash("Thankyou, Pub Successfully Added")
        return redirect(url_for("get_pubs")) 
    
    return render_template("add_pub.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
    