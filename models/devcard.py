import json


class DevCard:
    def __init__(self, item: dict,
                 nine_action: str,
                 nine_description: str,
                 nine_zombies: int,
                 nine_health: int,
                 ten_action: str,
                 ten_description: str,
                 ten_zombies: int,
                 ten_health: int,
                 eleven_action: str,
                 eleven_description: str,
                 eleven_zombies: int,
                 eleven_health: int,
                 ):
        self.item = item
        self.nine_info = {"action": nine_action,
                          "description": nine_description,
                          "zombies": nine_zombies,
                          "health_change": nine_health}
        self.ten_info = {"action": ten_action,
                         "description": ten_description,
                         "zombies": ten_zombies,
                         "health_change": ten_health}
        self.eleven_info = {"action": eleven_action,
                            "description": eleven_description,
                            "zombies": eleven_zombies,
                            "health_change": eleven_health}

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __repr__(self):
        return self.__str__()

    # based on https://changsin.medium.com/how-to-serialize-a-class-object-to-json-in-python-849697a0cd3
    def __iter__(self):
        yield from {
            "item": self.item,
            "nine_info": self.nine_info,
            "ten_info": self.nine_info,
            "eleven_info": self.nine_info
        }.items()