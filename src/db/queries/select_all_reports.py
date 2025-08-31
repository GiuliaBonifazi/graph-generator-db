from db.models import Report

def select_all_reports():
    return Report.query.all()