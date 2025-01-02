def individual_data(todo):
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "status": todo["is_done"],
    }

def all_data(todos):
    return[individual_data(todo) for todo in todos]