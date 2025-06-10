
_TYPE_LABELS = {
    list:  "List",
    tuple: "Tuple",
    set:   "Set",
    dict:  "Dict",
}

def all_thing_is_obj(object: any) -> int:
    if isinstance(object, str):
        print(f"{object} is in the kitchen : <class 'str'>")
    elif type(object) in _TYPE_LABELS:
        print(f"{_TYPE_LABELS[type(object)]}: {type(object)}")
    else:
        print("Type not found")
    return 42