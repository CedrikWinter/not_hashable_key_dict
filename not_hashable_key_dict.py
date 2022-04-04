
class NotHashableKeyDictException(Exception):
    pass


class NotHashableKeyDict():

    def __init__(self, *args):
        values = [self.__create_element(key, value) for key, value in args]
        self.__values__ = values

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return len(self.__values__)

    def __delitem__(self, key):
        keys = self.keys()

        if key in keys:
            index = keys.index(key)
            del self.__values__[index]

    def clear(self):
        self.__values__ = []

    def copy(self):
        items = [
            (key_value["key"], key_value["value"])
            for key_value in self.__values__
        ]

        return self.__class__(*items)

    def has_key(self, k):
        return k in self.keys()

    def update(self, *args, **kwargs):
        if kwargs:
            raise NotHashableKeyDictException(f"no kwargs allowed in '{self.__class__.__name__}.update' method")
        for key, value in args:
            self[key] = value

        return self.items()

    def updateKey(self, key, value):
        previous = self.get(key, {})
        if not(isinstance(previous, dict) and isinstance(value, dict)):
            raise NotHashableKeyDictException(
                f"previous value and value must be 'dict'. "
                f"previous value={previous} ({type(previous)}), "
                f"value={value} ({type(value)})"
            )
        return self.set(key, {**previous, **value})

    def __repr__(self) -> list:
        return repr(self.items())

    @classmethod
    def __create_element(cls, key, value):
        return {"key": key, "value": value}

    def set(self, key, value) -> None:
        keys = self.keys()

        if key in keys:
            index = keys.index(key)
            self.__values__[index] = self.__create_element(key, value)
        else:
            self.__values__.append(self.__create_element(key, value))

        return self.items()

    def keys(self):
        return [dict_key_value["key"] for dict_key_value in self.__values__]

    def values(self):
        return [value["value"] for value in self.__values__]

    def items(self):
        return [(dict_key_value["key"], dict_key_value["value"]) for dict_key_value in self.__values__]

    def pop(self, key, default=None):
        keys = self.keys()

        if key in keys:
            index = keys.index(key)
            value = self.__values__.pop(index)["value"]
        else:
            value = default

        return value

    def get(self, key, default=None):
        keys = self.keys()

        if key in keys:
            index = keys.index(key)
            value = self.__values__[index]["value"]
        else:
            value = default

        return value

    def setdefault(self, key, value=None):
        if key not in self.keys():
            self.set(key, value)

        return self.get(key)

    def __iter__(self):
        return iter(self.keys())
