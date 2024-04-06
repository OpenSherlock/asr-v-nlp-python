from json import dumps

def check_json(ob, path=""):
    try:
        dumps(ob)
        return None, True
    except TypeError:
        if not isinstance(ob, dict):
            return path, ob
        for k, v in ob.items():
            p, v = check_json(v, f"{path}/{k}")
            if v is not True:
                return p, v
