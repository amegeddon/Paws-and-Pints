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
    pubs_cursor = mongo.db.pubs.find()
    pubs = list(pubs_cursor)
    print("Number of pubs fetched:", len(pubs))
    print("Pubs data:", pubs)

    for pub in pubs:
        pub_id_str = str(pub['_id'])  
        pub_reviews_cursor = mongo.db.reviews.find({'pub_id': pub_id_str})
        pub_reviews = list(pub_reviews_cursor)
        pub['reviews'] = pub_reviews
        
        total_ratings = 0
        num_reviews = 0
        for review in pub_reviews:
            total_ratings += int(review['user_rating'])
            num_reviews += 1
        
        if num_reviews > 0:
            pub['average_rating'] = total_ratings / num_reviews
        else:
            pub['average_rating'] = 0
        
        print(f"Pub ID: {pub_id_str}, Total Ratings: {total_ratings}, Num Reviews: {num_reviews}, Average Rating: {pub['average_rating']}")

    return render_template("reviews.html", pubs=pubs)






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
    # Grab the session user's username from db
    session_username = mongo.db.users.find_one({"username": session["user"]})["username"]
    print("Session Username:", session_username)

    if session_username:
        print("Session user is:", session_username)
        # Check if the user is logged in
        if 'user' not in session or session['user'] != username:
            print("User not logged in or session user doesn't match URL username")
            return redirect(url_for('login'))

        # Query the database for the user
        user = mongo.db.users.find_one({"username": username})
        print("User:", user)

        if not user:
            print("User not found")
            return "User not found"

        # Fetch the user's reviews from the database
        user_reviews = list(mongo.db.reviews.find({"user_id": user["_id"]}))
        print("User Reviews:", user_reviews)

        # Check if user_reviews contain more than just the title
        if user_reviews:
            first_review = user_reviews[0]
            print("First Review:", first_review)

        # Render the profile page template with the user's reviews
        return render_template("profile.html", username=username, user_reviews=user_reviews)

    return redirect(url_for("login"))





@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


from flask import session

@app.route('/write_review', methods=["GET", "POST"])
def write_review():
    if request.method == "POST":
        
        session_username = mongo.db.users.find_one({"username": session["user"]})["username"]
        
        if not session_username:
            return redirect(url_for("login"))  
        
        # Query the database for the user
        user = mongo.db.users.find_one({"username": session_username})
        
        title = request.form.get('title')
        review_text = request.form.get('review_text')
        user_rating = request.form.get('user_rating')
        pub_id = request.form.get('pub_id')
        user_id = user["_id"]  # Store the ObjectId of the user
        
        review_data = {
            "title": title,
            "review_text": review_text,
            "user_rating": user_rating,
            "pub_id": pub_id,
            "user_id": user_id 
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


@app.route("/confirm_delete_review/<review_id>", methods=["GET", "POST"])
def confirm_delete_review(review_id):
    if request.method == "POST":
        try:
            review_id_obj = ObjectId(review_id)
        except Exception as e:
            flash("Invalid review ID")
            return redirect(url_for("profile", username=session['user']))

        review = mongo.db.reviews.find_one({"_id": review_id_obj})
        if not review:
            flash("Review not found")
            return redirect(url_for("profile", username=session['user']))

        return render_template("confirm_delete_review.html", review=review)
    else:
        flash("Invalid request method")
        return redirect(url_for("profile", username=session['user']))



@app.route("/delete_review/<review_id>", methods=["POST"])
def delete_review(review_id):
    try:
        review_id_obj = ObjectId(review_id)
    except Exception as e:
        flash("Invalid review ID")
        return redirect(url_for("profile", username=session['user']))

    result = mongo.db.reviews.delete_one({"_id": review_id_obj})
    if result.deleted_count == 0:
        flash("Review not found")
    else:
        flash("Review Successfully Deleted")

    return redirect(url_for("profile", username=session['user']))

# Iterate over endpoint names
for rule in app.url_map.iter_rules():
    print(rule.endpoint)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        # Check if user is logged in
        if "user" not in session or session["user"] is None:
            flash("Please log in to edit a review.")
            return redirect(url_for("login"))

        
        user = mongo.db.users.find_one({"username": session["user"]})
        if user is None:
            flash("User not found.")
            return redirect(url_for("login"))

        
        title = request.form.get('title')
        review_text = request.form.get('review_text')
        user_rating = request.form.get('user_rating')
        pub_id = request.form.get('pub_id')

        
        user_id = user["_id"]

        
        review_data = {
            "title": title,
            "review_text": review_text,
            "user_rating": user_rating,
            "pub_id": pub_id,
            "user_id": user_id
        }

        
        username = session.get("user")
        try:
            mongo.db.reviews.update_one({"_id": ObjectId(review_id)}, {"$set": review_data})
            flash("Review successfully updated.")
            return redirect(url_for("profile", username=username))   
        except Exception as e:
            flash("An error occurred while updating the review.")
            app.logger.error(f"Error updating review: {e}")
            return redirect(url_for("profile", username=username))
        
    else:
            
        review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
        return render_template("edit_review.html", review=review)
    

@app.route("/cancel_edit_review")
def cancel_edit_review():
    # Redirect the user to their profile page
     return redirect(url_for("profile", username=username))
 
 
@app.route("/manage_reviews")
def manage_reviews():
    print("Manage reviews route accessed.")
    pubs_cursor = mongo.db.pubs.find()
    pubs = list(pubs_cursor)
    print("Number of pubs fetched:", len(pubs))
    print("Pubs data:", pubs)

    for pub in pubs:
        pub_id_str = str(pub['_id'])  
        pub_reviews_cursor = mongo.db.reviews.find({'pub_id': pub_id_str})
        pub_reviews = list(pub_reviews_cursor)
        pub['reviews'] = pub_reviews
        
        total_ratings = 0
        num_reviews = 0
        for review in pub_reviews:
            total_ratings += int(review['user_rating'])
            num_reviews += 1
        
        if num_reviews > 0:
            pub['average_rating'] = total_ratings / num_reviews
        else:
            pub['average_rating'] = 0
        
        print(f"Pub ID: {pub_id_str}, Total Ratings: {total_ratings}, Num Reviews: {num_reviews}, Average Rating: {pub['average_rating']}")

    return render_template("manage_reviews.html", pubs=pubs)


@app.route("/delete_pub/<pub_id>", methods=["POST"])
def delete_pub(pub_id):
    print("Delete Pub route accessed.")
    try:
        pub_id_obj = ObjectId(pub_id)
    except Exception as e:
        flash("Invalid pub ID")
        return redirect(url_for("manage_reviews"))
    
    result = mongo.db.pubs.delete_one({"_id": pub_id_obj})
    if result.deleted_count == 0:
        flash("Pub not found")
    else:
        flash("Pub Successfully Deleted")
    
    return redirect(url_for("manage_reviews"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
    