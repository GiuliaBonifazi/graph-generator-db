def criterion_to_json(criterion):
    return {
        "name": criterion.name,
        "description": criterion.description,
        "id": criterion.id
    }