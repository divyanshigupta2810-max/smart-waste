from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():

    admin = User.query.filter_by(
        email="admin@smartwaste.com"
    ).first()

    if admin:
        print("Admin already exists.")

    else:
        admin = User(
            name="Smart Waste Admin",
            email="admin@smartwaste.com",
            role="admin"
        )

        admin.set_password("Admin@123")

        db.session.add(admin)
        db.session.commit()

        print("Admin account created successfully!")

