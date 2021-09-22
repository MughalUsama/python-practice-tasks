def singleton(_class):
    created_objects = {}

    def get_instance(*args, **kwargs):
        if _class not in created_objects:
            created_objects[_class] = _class(*args, **kwargs)
        return created_objects[_class]

    return get_instance


@singleton
class SampleClass:
    def __init__(self, x, y):
        self.id = x
        self.name = y


if __name__ == "__main__":
    obj1 = SampleClass(5, "1st Object")
    obj2 = SampleClass(6, "2nd Object")

    print("Object 1:", obj1.name, obj1)
    print("Object 2:", obj2.name, obj2)
