NESTED = "nested"
UNCHANGED = "unchanged"
ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"


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
        else:
            value1 = data1[key]
            value2 = data2[key]

            if isinstance(value1, dict) and isinstance(value2, dict):
                diff.append({
                    "key": key,
                    "type": NESTED,
                    "children": build_diff(value1, value2)
                })
            elif value1 == value2:
                diff.append({
                    "key": key,
                    "type": UNCHANGED,
                    "value": value1
                })
            else:
                diff.append({
                    "key": key,
                    "type": CHANGED,
                    "old_value": value1,
                    "new_value": value2
                })

    return diff
