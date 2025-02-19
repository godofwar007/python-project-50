from gendiff.constants import ADDED, CHANGED, NESTED, REMOVED, UNCHANGED


def build_diff(data1, data2):
    keys = sorted(set(data1) | set(data2))
    diff = []

    for key in keys:
        if key not in data1:
            diff.append({
                "key": key,
                "type": ADDED,
                "value": data2[key]
            })
        elif key not in data2:
            diff.append({
                "key": key,
                "type": REMOVED,
                "value": data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                "key": key,
                "type": NESTED,
                "children": build_diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            diff.append({
                "key": key,
                "type": UNCHANGED,
                "value": data1[key]
            })
        else:
            diff.append({
                "key": key,
                "type": CHANGED,
                "old_value": data1[key],
                "new_value": data2[key]
            })

    return diff
