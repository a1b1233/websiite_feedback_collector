from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///admins.db"
db = SQLAlchemy(app)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///feedback.db"
app.secret_key = "1615"
db = SQLAlchemy(app)

EMAIL_ADDRESS = "gs7august2005@gmail.com"  
EMAIL_PASSWORD = "eokn xsyv uvnw umht"      

def send_email(to, subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {to}")
    except Exception as e:
        print(f"Failed to send email: {e}")

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(10), nullable=False )
    feedback = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default="Not Resolved")

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

    subject = "Thank you for your feedback!"
    body = f"Hi {name},\n\nThank you for submitting your feedback. We have received it and will get back to you soon.\n\nYour Feedback:\nRating: {rating}\nComment: {feedback}\n\nRegards,\nSupport Team"
    send_email(email, subject, body)

    return redirect(url_for("thank_you"))

@app.route("/thank-you", methods=["GET"])
def thank_you():
    return render_template("thank_you.html")

@app.route("/return-home", methods=["GET"])
def return_home():
    return redirect(url_for("home"))

@app.route("/update-status/<int:id>", methods=["POST"])
def update_status(id):
    new_status = request.form["status"]
    feedback_entry = Feedback.query.get(id)
    if feedback_entry:
        feedback_entry.status = new_status
        db.session.commit()

        subject = "Your Feedback Status has been resolved"
        body = f"Hi {feedback_entry.name},\n\nYour feedback status has been updated to '{new_status}'.\n\nThank you for your patience.\n\nRegards,\nSupport Team"
        send_email(feedback_entry.email, subject, body)

    return redirect(url_for("admin_dashboard"))

@app.route("/check-status", methods=["GET"])
def check_status_page():
    return render_template("check_status.html")

@app.route("/check-feedback", methods=["POST"])
def check_feedback():
    name = request.form["name"].strip()
    email = request.form["email"].strip()

    feedback_entry = Feedback.query.filter_by(name=name, email=email).first()

    if feedback_entry:
        return render_template("feedback_status.html", feedback=feedback_entry)
    else:
        return render_template("feedback_status.html", feedback=None)
    
@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    error = None
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email == "gs7august@gmail.com" and password == "8052566305":
            return redirect(url_for("admin_dashboard"))
    return render_template("admin_login.html" )

@app.route("/admin-dashboard", methods=["GET"])
def admin_dashboard():
    feedback_data = Feedback.query.all()
    return render_template("admin-dashboard.html", feedback_data=feedback_data)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

