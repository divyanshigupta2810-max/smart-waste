from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
import uuid
from flask_login import current_user
from app.models import User, Complaint
from flask_login import (
    login_user,
    logout_user,
    login_required
)

from app import db


main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html")

@main.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered.")
            return redirect(url_for("main.register"))

        user = User(
            name=name,
            email=email,
            role="citizen"
        )

        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Registration successful. Please login.")
        return redirect(url_for("main.login_choice"))

    return render_template("register.html")


@main.route("/login")
def login_choice():
    return render_template("login_choice.html")


@main.route("/user-login", methods=["GET", "POST"])
def user_login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(
            email=email
        ).first()

        if user and user.check_password(password):

            if user.role != "citizen":
                return "Please use Admin Login for this account.", 403

            login_user(user)

            return redirect(
                url_for("main.dashboard")
            )

        flash("Invalid user email or password.")

    return render_template("user_login.html")


@main.route("/admin-login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(
            email=email
        ).first()

        if user and user.check_password(password):

            if user.role != "admin":
                return "Please use User Login for this account.", 403

            login_user(user)

            return redirect(
                url_for("main.admin_dashboard")
            )

        flash("Invalid admin email or password.")

    return render_template("admin_login.html")

# =========================
# REPORT WASTE ISSUE
# =========================

@main.route("/report", methods=["GET", "POST"])
@login_required
def report():

    if current_user.role != "citizen":
        return "Access Denied", 403

    if request.method == "POST":

        category = request.form.get("category")
        description = request.form.get("description")

        # Priority based on category
        priority_data = {
            "Illegal Dumping": ("High", 90),
            "Garbage on Road": ("High", 80),
            "Overflowing Bin": ("Medium", 70),
            "Missed Collection": ("Medium", 60),
            "Other": ("Low", 40)
        }

        priority, score = priority_data.get(
            category,
            ("Medium", 50)
        )

        complaint_id = "SW-" + str(uuid.uuid4())[:8].upper()

        complaint = Complaint(
            complaint_id=complaint_id,
            user_id=current_user.id,
            category=category,
            description=description,
            priority=priority,
            priority_score=score,
            status="Submitted"
        )

        db.session.add(complaint)
        db.session.commit()

        return render_template(
            "complaint_success.html",
            complaint=complaint
        )

    return render_template("report.html")


# =========================
# TRACK COMPLAINT
# =========================

@main.route("/track", methods=["GET", "POST"])
@login_required
def track():

    complaint = None
    message = None

    if request.method == "POST":

        complaint_id = request.form.get("complaint_id")

        complaint = Complaint.query.filter_by(
            complaint_id=complaint_id,
            user_id=current_user.id
        ).first()

        if not complaint:
            message = "Complaint not found. Please check the Complaint ID."

    return render_template(
        "track.html",
        complaint=complaint,
        message=message
    )


@main.route("/admin")
@login_required
def admin_dashboard():

    if current_user.role != "admin":
        return "Access Denied", 403

    complaints = Complaint.query.order_by(
        Complaint.created_at.desc()
    ).all()

    total = Complaint.query.count()

    pending = Complaint.query.filter(
        Complaint.status != "Resolved"
    ).count()

    resolved = Complaint.query.filter_by(
        status="Resolved"
    ).count()

    high_priority = Complaint.query.filter_by(
        priority="High"
    ).count()

    return render_template(
        "admin_dashboard.html",
        complaints=complaints,
        total=total,
        pending=pending,
        resolved=resolved,
        high_priority=high_priority
    )

@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out successfully.")
    return redirect(url_for("main.home"))

# =========================
# ADMIN UPDATE STATUS
# =========================

@main.route("/admin/update/<int:complaint_id>", methods=["POST"])
@login_required
def update_complaint(complaint_id):

    if current_user.role != "admin":
        return "Access Denied", 403

    complaint = Complaint.query.get_or_404(complaint_id)

    new_status = request.form.get("status")

    complaint.status = new_status

    db.session.commit()

    return redirect(url_for("main.admin_dashboard"))

@main.route("/dashboard")
@login_required
def dashboard():

    if current_user.role != "citizen":
        return "Access Denied", 403

    return render_template("dashboard.html")