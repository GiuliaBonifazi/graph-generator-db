def criterion_to_json(criterion):
    return {
        "name": criterion.name,
        "description": criterion.description,
        "id": criterion.id
    }
    
def report_to_json(report):
    return {
        "id": report.id,
        "correct": report.correct,
        "level": report.level,
        "graph_type_name": report.graph_type_name,
        "criterion_id": report.criterion_id
    }