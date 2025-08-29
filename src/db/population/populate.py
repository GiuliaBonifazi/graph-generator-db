from db.models import GraphType, Criterion
from db.database import get_database
import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent
criteria_file_path = base_dir / "criteria.json"


def populate_graph_types():
    db = get_database()
    for type in ["Bar graph", "Pie chart", "Line graph"]:
        db.session.add(GraphType(name=type))
    db.session.commit()
    
def populate_criteria():
    db = get_database()
    criteria = json.load(open(criteria_file_path, "r"))
    for c in criteria:
        db.session.add(Criterion(name=c["name"], description=c["desc"]))
    db.session.commit()
    
def populate_all():
    populate_criteria()
    populate_graph_types()
    