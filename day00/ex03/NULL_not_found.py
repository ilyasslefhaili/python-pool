import math

def NULL_not_found(obj: any) -> int:
    if obj is None:
        label, text = "Nothing", "None"
    elif isinstance(obj, float) and math.isnan(obj):
        label, text = "Cheese", "nan"
    elif isinstance(obj, bool) and obj is False:
        label, text = "Fake", "False"
    elif isinstance(obj, int) and obj == 0:
        label, text = "Zero", "0"
    elif isinstance(obj, str) and obj == "":
        print(f"Empty: {type(obj)}")
        return 0
    else:
        print("Type not Found")
        return 1

    print(f"{label}: {text} {type(obj)}")
    return 0
