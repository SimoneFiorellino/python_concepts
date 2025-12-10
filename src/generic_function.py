"""
@singledispatch A form of function overloading where a single generic function dynamically selects
the appropriate implementation based on the runtime type of its first argument.

Here, a mechanism that selects a function implementation based on the type of its first argument,
enabling clean, extensible type-specific behavior such as custom serialization.

Source: Tech With Tim
"""

import json
from functools import singledispatch
from datetime import datetime


class User:
    def __init__(self, name, age, join_date):
        self.name = name
        self.age = age
        self.join_date = join_date


@singledispatch
def serialize(obj):
    raise NotImplementedError(f"Cannot serialize object of type {type(obj).__name__}")


@serialize.register
def _(user: User):
    return {"name": user.name, "age": user.age, "join_date": user.join_date.isoformat()}


@serialize.register
def _(dt: datetime):
    return dt.isoformat()


@serialize.register
def _(obj: set):
    return list(obj)


# Example usage
if __name__ == "__main__":
    data = {
        "user": User("Alice", 30, datetime(2020, 5, 17)),
        "created_at": datetime.now(),
        "tags": {"python", "serialization", "example"},
    }

    json_data = json.dumps(data, default=serialize, indent=4)
    print(json_data)
