from db.models import Criterion

def select_all_criteria():
    return Criterion.query.all()