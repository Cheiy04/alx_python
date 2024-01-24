from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

# Connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_username}:{db_password}@{db_host}/{db_name}"

db = SQLAlchemy(app)

# Define your USER Model class here
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables

# Root route
@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

# New route to add a user
@app.route('/add_user', methods=['GET', 'POST'], strict_slashes=False)
def add_user():
    if request.method == 'POST':
        # Retrieve name and email from the submitted form data
        name = request.form.get('name')
        email = request.form.get('email')

        try:
            # Attempt to insert the new user into the User table
            new_user = User(name=name, email=email) # type: ignore
            db.session.add(new_user)
            db.session.commit()

            # Flash success message on successful insertion
            flash("User added successfully!", "success")
        except Exception as e:
            # Handle exceptions (e.g., duplicate email) by flashing an appropriate error message
            db.session.rollback()
            flash(f"Error adding user: {str(e)}", "error")

        return redirect(url_for('add_user'))

    # For GET requests, render the add_user.html template
    return render_template('add_user.html')

# Route to retrieve and display all users
@app.route('/users', strict_slashes=False)
def display_users():
    # Connect to the alx_flask_db database
    db.init_app(app)

    # Retrieve all users from the User table
    users = User.query.all()

    # Render the results using the 8-users.html template
    return render_template('users.html', users=users)

# Update a User
@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get(user_id)

    if user is None:
        flash("User not found!", "error")
        return redirect(url_for('display_users'))

    if request.method == 'POST':
        # Extract the updated name and email from the form data
        updated_name = request.form.get('name')
        updated_email = request.form.get('email')

        # Validate the data: ensure both fields are provided
        if not updated_name or not updated_email:
            flash("Name and Email are required!", "error")
        else:
            # Use the given user_id to identify and update the corresponding user
            user.name = updated_name
            user.email = updated_email

            try:
                # If the update is successful, flash the message
                db.session.commit()
                flash("User updated successfully!", "success")
            except Exception as e:
                # In the case of errors, provide a relevant error message
                db.session.rollback()
                flash(f"Error updating user: {str(e)}", "error")

    # For GET requests, render the update_user.html template
    return render_template('update_user.html', user=user)

# Delete a User
@app.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if user is None:
        flash("User not found!", "error")
        return redirect(url_for('display_users'))

    if request.method == 'POST':
        try:
            # On accessing this route, remove the user with the specified user_id
            db.session.delete(user)
            db.session.commit()

            # After successful deletion, display the message
            flash("User deleted successfully!", "success")
        except Exception as e:
            # Handle potential database errors and exceptions with care
            db.session.rollback()
            flash(f"Error deleting user: {str(e)}", "error")

        return redirect(url_for('display_users'))

    # For GET requests, render the delete_user.html template
    return render_template('delete_user.html', user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
