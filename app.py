from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///admins.db"
db = SQLAlchemy(app)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///feedback.db"
app.secret_key = "1615"
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(10), nullable=False)
    feedback = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    name = request.form["name"]
    email = request.form["email"]
    rating = request.form["rating"]
    feedback = request.form["feedback"]
    new_feedback = Feedback(name=name,email=email,rating=rating,feedback=feedback)
    db.session.add(new_feedback)
    db.session.commit()
    return redirect(url_for("thank_you"))

@app.route("/thank-you", methods=["GET"])
def thank_you():
    return render_template("thank_you.html")

@app.route("/return-home", methods=["GET"])
def return_home():
    return redirect(url_for("home"))

@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email == "gs7august@gmail.com" and password == "8052566305":
            return redirect(url_for("admin_dashboard"))
    return render_template("admin_login.html")

@app.route("/admin-dashboard", methods=["GET"])
def admin_dashboard():
    feedback_data = Feedback.query.all()
    return render_template("admin-dashboard.html", feedback_data=feedback_data)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

