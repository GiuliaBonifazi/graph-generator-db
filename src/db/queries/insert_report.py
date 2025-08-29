from db.database import get_database

def insert_report(report):
    db = get_database()
    db.session.add(report)