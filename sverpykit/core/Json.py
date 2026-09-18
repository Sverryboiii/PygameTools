import json

def read_json(path: str, obj: int | str | None = None) -> dict | list | int | str:
    with open(path, "r") as f:
        data = json.load(f)
    return data.get(obj, data)

def write_json(path: str, obj: dict | list) -> None:
    with open(path, "w") as f:
        json.dump(obj, f, indent=4)

def update_json(path: str, obj: dict | list) -> None:
    with open(path, "r") as f:
        data: list | dict = json.load(f)
    if not isinstance(obj, type(data)):
        raise ValueError("Object does not have the same type as JSON file!")
    with open(path, "w") as f:
        data.update(obj) if isinstance(data, dict) else data.extend(obj)
        json.dump(data, f, indent=4)