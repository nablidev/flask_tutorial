"""Application routes."""
from datetime import datetime as dt

from flask import current_app as app
from flask import make_response, redirect, render_template, request, url_for

from .models import User, db


@app.route("/", methods=["GET", "POST"])
def user_records():
    """Create a user via query string parameters."""
    #username = request.args.get("user")
    #email = request.args.get("email")
    if request.method == "POST":

        if request.form['action'] == "delete":
            h_user = request.form['h_user']
            User.query.filter_by(username=h_user).delete()
            db.session.commit()
        else:
            username = request.form['user']
            email = request.form['email']

            if username and email:
                existing_user = User.query.filter(
                    User.username == username or User.email == email
                ).first()
                if existing_user:
                    return make_response(f"{username} ({email}) already created!")
                new_user = User(username=username, email=email, created=dt.now(),
                    bio="my cool bio",
                    admin=False,
                )  # Create an instance of the User class
                db.session.add(new_user)  # Adds new User record to database
                db.session.commit()  # Commits all changes
                redirect(url_for("user_records"))

    return render_template("users.html", users=User.query.all(), title="Show Users")