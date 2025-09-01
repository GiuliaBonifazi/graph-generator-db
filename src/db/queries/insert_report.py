from db.database import get_database
from db.models import Report

def insert_report(report):
    db = get_database()
    db.session.add(Report(
        correct=report["correct"],
        level=report["level"],
        graph_type_name=report["graph_type_name"],
        criterion_id=report["criterion_id"]
    ))
    db.session.commit()