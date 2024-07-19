import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, send_file)
from flask_pymongo import PyMongo
from io import BytesIO
from bson import Binary
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Code taken from Stackoverflow
@app.errorhandler(404)
def page_not_found(error):
    """
    Handles 404 errors and renders the 404 page.
    """
    return render_template('404.html'), 404


@app.route("/")
@app.route("/get_pubs")
def get_pubs():
    """
    Retrieves and displays a list of pubs with their reviews and average ratings.
    """
    pubs_cursor = mongo.db.pubs.find()
    pubs = list(pubs_cursor)

    for pub in pubs:
        pub_id_str = str(pub['_id'])
        pub_reviews_cursor = mongo.db.reviews.find({'pub_id': pub_id_str})
        pub_reviews = list(pub_reviews_cursor)
        pub['reviews'] = pub_reviews
        total_ratings = 0
        num_reviews = 0

        for review in pub_reviews:
            user_rating = review.get('user_rating')
            if user_rating is not None:
                try:
                    total_ratings += int(user_rating)
                    num_reviews += 1
                except ValueError:
                    print(f"Invalid rating value: {user_rating}")

        avg_rating = total_ratings / num_reviews if num_reviews > 0 else 0
        pub['average_rating'] = avg_rating

    return render_template("reviews.html", pubs=pubs)



@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Handles user registration, including checking for existing usernames,
    creating new user accounts, and redirecting to the profile page.
    """
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
    """
    Handles user login, verifying credentials and redirecting to the profile page
    upon successful login or displaying an error message for invalid credentials.
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                 existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back, {}".format(
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
    """
    Displays the profile page for the specified username if the user is logged in.
    Redirects to the login page if the user is not logged in or if the session user
    does not match the URL username.
    """
    # Check if user is logged in
    if 'user' not in session:
        print("User not logged in")
        return redirect(url_for('login'))

    # Grab the session user's username from db
    session_username = mongo.db.users.find_one({"username": session["user"]})["username"]

    if session_username:
        print("Session user is:", session_username)
        # Check if the session user matches the URL username
        if session_username != username:
            print("Session user doesn't match URL username")
            flash('Please log in to view this page', 'warning')
            return redirect(url_for('login'))

        # Query the database for the user
        user = mongo.db.users.find_one({"username": username})

        if not user:
            print("User not found")
            return "User not found"

        user_reviews = list(mongo.db.reviews.find({"user_id": user["_id"]}))

        if user_reviews:
            first_review = user_reviews[0]
        user_pubs = list(mongo.db.pubs.find({"user_id": user["_id"]}))
        
        return render_template(
         "profile.html",
         username=username,
         user_reviews=user_reviews,
         user_pubs=user_pubs
        )

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Logs out the current user by removing them from the session cookie.
    Redirects to the login page with a logout confirmation message.
    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route('/write_review', methods=["GET", "POST"])
def write_review():
    """
    Handles review submission for logged-in users. 
    - POST: Adds the review to the database and redirects to the pubs page.
    - GET: Renders the review form with the pub ID.
    """
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        session_username = session["user"]
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
    """
    Handles adding a new pub for logged-in users.
    - POST: Validates and saves pub details to the database; redirects to photo upload page.
    - GET: Renders the pub addition form.
    """
    # Check if user is logged in
    if "user" not in session or session["user"] is None:
        flash("Please log in to add a pub.")
        return redirect(url_for("login"))

    user = mongo.db.users.find_one({"username": session["user"]})
    if user is None:
        flash("User not found.")
        return redirect(url_for("login"))
    user_id = user.get('_id')

    if request.method == "POST":
        pub_name = request.form.get("name")
        pub_location = request.form.get("location")
        pub_description = request.form.get("description")
        food_served = request.form.get("food_served") == "yes"
        dogs_allowed = request.form.get("dogs_allowed") == "yes"
        water_provided = request.form.get("water_provided") == "yes"
        dog_meals = request.form.get("dog_meals") == "yes"
        nearby_walks = request.form.get("nearby_walks") == "yes"
        loving_staff = request.form.get("loving_staff") == "yes"

        pub_data = {
            "name": pub_name,
            "location": pub_location,
            "description": pub_description,
            "food_served": food_served,
            "dogs_allowed": dogs_allowed,
            "water_provided": water_provided,
            "dog_meals": dog_meals,
            "nearby_walks": nearby_walks,
            "loving_staff": loving_staff,
            "user_id": user_id
        }

        # Insert the pub into the database
        try:
            result = mongo.db.pubs.insert_one(pub_data)
            pub_id = result.inserted_id
        except Exception as e:
            print("Error inserting pub:", e)
            flash("Error adding pub. Please try again.")
            return redirect(url_for("add_pub"))

        return redirect(url_for("photo_upload", pub_id=pub_id))

    return render_template("add_pub.html")


@app.route("/confirm_delete_review/<review_id>", methods=["GET", "POST"])
def confirm_delete_review(review_id):
    """
    Handles review deletion confirmation.
    - POST: Validates review ID, retrieves review, and renders confirmation page.
    - GET: Returns an error if accessed with GET method.
    """
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
    """
    Deletes a review based on the provided review ID.
    - Validates the review ID.
    - Attempts to delete the review from the database.
    - Provides feedback on success or failure.
    - Redirects to the user's profile page.
    """
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



@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """
    Allows users to edit their own reviews.
    - Checks if the user is logged in and authorized.
    - Handles both GET (for displaying the review form) and POST (for updating the review).
    - Provides feedback on success or failure and redirects to the user's profile.
    """
    # Check if user is logged in
    if "user" not in session or session["user"] is None:
        flash("Please log in to edit a review.")
        return redirect(url_for("login"))

    user = mongo.db.users.find_one({"username": session["user"]})
    if user is None:
        flash("User not found.")
        return redirect(url_for("login"))

    if request.method == "POST":
        # Retrieve the review from the database
        review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
        # Prevent unauthorized access to review editing
        if review and user["_id"] != review["user_id"]:
            flash("You are not authorized to edit this review.")
            return redirect(url_for("get_pubs"))

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
            mongo.db.reviews.update_one(
                {"_id": ObjectId(review_id)},
                {"$set": review_data}
            )
            flash("Review successfully updated.")
            return redirect(url_for("profile", username=username))

        except Exception as e:
            flash("An error occurred while updating the review.")
            app.logger.error(f"Error updating review: {e}")
            return redirect(url_for("profile", username=username))

    else:  # GET request for editing review
        # Retrieve the review from the database
        review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
        if review and user["_id"] != review["user_id"]:
            flash("You are not authorized to edit this review.")
            return redirect(url_for("get_pubs"))

        return render_template("edit_review.html", review=review)

    
@app.route("/cancel_edit_review")
def cancel_edit_review():
    """
    Redirects the user to their profile page when canceling an edit review action.
    """
    # Redirect the user to their profile page
    return redirect(url_for("profile", username=username))

 
@app.route("/manage_reviews")
def manage_reviews():
    """
    Retrieves and displays a list of pubs along with their reviews and average ratings.
    """
    pubs_cursor = mongo.db.pubs.find()
    pubs = list(pubs_cursor)

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
        
    return render_template("manage_reviews.html", pubs=pubs)


@app.route("/delete_pub/<pub_id>", methods=["POST"])
def delete_pub(pub_id):
    """
    Deletes a pub from the database based on the provided pub ID.
    Redirects to the manage reviews page with a success or error message.
    """
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


@app.route("/confirm_delete_pub/<pub_id>", methods=["GET", "POST"])
def confirm_delete_pub(pub_id):
    """
    Displays a confirmation page for deleting a pub.
    If the request method is POST, validates the pub ID and retrieves the pub details.
    Redirects to the manage reviews page on invalid requests or errors.
    """
    print("Confirm Delete Pub route accessed.")
    print("Pub ID:", pub_id)
    if request.method == "POST":
        try:
            pub_id_obj = ObjectId(pub_id)
        except Exception as e:
            flash("Invalid pub ID")
            return redirect(url_for("manage_reviews"))

        pub = mongo.db.pubs.find_one({"_id": pub_id_obj})
        if not pub:
            flash("Pub not found")
            return redirect(url_for("manage_reviews"))

        return render_template("confirm_delete_pub.html", pub=pub)
    else:
        flash("Invalid request method")
        return redirect(url_for("manage_reviews"))


@app.route("/edit_pub/<pub_id>", methods=["GET", "POST"])
def edit_pub(pub_id):
    """
    Allows a logged-in user to edit a pub's details.
    On POST request, updates pub information and redirects to photo editing.
    On GET request, displays the current pub details for editing.
    """
    # Check if user is logged in
    if "user" not in session or session["user"] is None:
        flash("Please log in to edit a pub.")
        return redirect(url_for("login"))

    user = mongo.db.users.find_one({"username": session["user"]})
    if user is None:
        flash("User not found.")
        return redirect(url_for("login"))

    if request.method == "POST":
        # Retrieve the pub from the database
        pub = mongo.db.pubs.find_one({"_id": ObjectId(pub_id)})
        # Prevents unauthorized access to pub editing
        if pub and user["_id"] != pub["user_id"]:
            flash("You are not authorized to edit this pub.")
            return redirect(url_for("get_pubs"))

        # Update pub details
        pub_name = request.form.get("name")
        pub_location = request.form.get("location")
        pub_description = request.form.get("description")
        food_served = request.form.get("food_served") == "yes"
        dogs_allowed = request.form.get("dogs_allowed") == "yes"
        water_provided = request.form.get("water_provided") == "yes"
        dog_meals = request.form.get("dog_meals") == "yes"
        nearby_walks = request.form.get("nearby_walks") == "yes"
        loving_staff = request.form.get("loving_staff") == "yes"

        pub_data = {
            "name": pub_name,
            "location": pub_location,
            "description": pub_description,
            "food_served": food_served,
            "dogs_allowed": dogs_allowed,
            "water_provided": water_provided,
            "dog_meals": dog_meals,
            "nearby_walks": nearby_walks,
            "loving_staff": loving_staff,
            "user_id": user["_id"]
        }

        username = session.get("user")
        try:
            mongo.db.pubs.update_one(
             {"_id": ObjectId(pub_id)},
             {"$set": pub_data}
            )

            flash("Pub successfully updated.")
        except Exception as e:
            flash("An error occurred while updating the pub.")
            app.logger.error(f"Error updating pub: {e}")
            return redirect(url_for("profile", username=username))

        # Redirect to page for editing photo
        return redirect(url_for("edit_photo", pub_id=pub_id))

    else:
        # Retrieve the pub from the database
        pub = mongo.db.pubs.find_one({"_id": ObjectId(pub_id)})
        if pub and user["_id"] != pub["user_id"]:
            flash("You are not authorized to edit this pub.")
            return redirect(url_for("get_pubs"))

        return render_template("edit_pub.html", pub=pub)


@app.route("/photo_upload/<pub_id>", methods=["GET", "POST"])
def photo_upload(pub_id):
    """
    Handles photo upload for a specific pub.
    On POST request, saves the uploaded image to the database and redirects to the user profile.
    On GET request, displays the photo upload form.
    """
    pub = mongo.db.pubs.find_one({"_id": ObjectId(pub_id)})

    if request.method == "POST":
        uploaded_file = request.files.get('photo')

        if uploaded_file:
            # Read the contents of the uploaded file as binary data
            file_data = uploaded_file.read()

            photo_data = {
                "filename": uploaded_file.filename,
                "data": Binary(file_data),
                "pub_id": ObjectId(pub_id)
            }
            mongo.db.photos.insert_one(photo_data)
            
            flash('Image successfully uploaded!', 'success')

            return redirect(url_for("profile", username=session.get("user")))

    return render_template("photo_upload.html", pub=pub)


@app.route("/photo/<pub_id>")
def get_photo(pub_id):
    """
    Retrieves and serves the photo associated with a specific pub ID.
    If no photo is found, serves a default image instead.
    """
    photo_data = mongo.db.photos.find_one({"pub_id": ObjectId(pub_id)})

    if photo_data:
        return send_file(BytesIO(photo_data["data"]), mimetype='image/jpeg')
    else:
        return send_file("static/images/bunny.jpg", mimetype='image/jpeg')


@app.route("/edit_photo/<pub_id>", methods=["GET", "POST"])
def edit_photo(pub_id):
    """
    Allows users to upload or update a photo for a specific pub.
    If a photo is uploaded, it replaces the existing photo or adds a new one.
    """
    pub = mongo.db.pubs.find_one({"_id": ObjectId(pub_id)})

    if request.method == "POST":
        uploaded_file = request.files.get('photo')

        if uploaded_file:
            # Read the contents of the uploaded file as binary data
            file_data = uploaded_file.read()

            photo_data = {
                "filename": uploaded_file.filename,
                "data": Binary(file_data),
                "pub_id": ObjectId(pub_id)
            }

        result = mongo.db.photos.update_one({"pub_id": ObjectId(pub_id)}, {
            "$set": photo_data},
            upsert=True)
        return redirect(url_for("profile", username=session.get("user")))

    return render_template("edit_photo.html", pub=pub)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)