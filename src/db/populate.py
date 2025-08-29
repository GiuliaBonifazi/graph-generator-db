from db.models import GraphType
from db.database import get_database


def populate_graph_types():
    db = get_database()
    for type in ["Bar graph", "Pie chart", "Line graph"]:
        db.session.add(GraphType(name=type))
    db.session.commit()
    
def populate_criteria():
    db = get_database()
    