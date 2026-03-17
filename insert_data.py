from app import app
from models.models import db, Book

with app.app_context():
    db.session.add_all(
        [
            Book("Deep Work", "Cal Newport", 24.99),
            Book("Designing Data-Intensive Applications", "Martin Kleppmann", 49.99),
            Book("Refactoring", "Martin Fowler", 39.99),
        ]
    )
    db.session.commit()
    print("Inserted")
