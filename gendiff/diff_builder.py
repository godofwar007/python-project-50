def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        if key in data1 and key in data2:
            value1 = data1[key]
            value2 = data2[key]
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff.append({
                    "key": key,
                    "type": "nested",
                    "children": build_diff(value1, value2)
                })
            elif value1 == value2:
                diff.append({
                    "key": key,
                    "type": "unchanged",
                    "value": value1
                })
            else:
                diff.append({
                    "key": key,
                    "type": "changed",
                    "old_value": value1,
                    "new_value": value2
                })
        elif key in data1:
            diff.append({
                "key": key,
                "type": "removed",
                "value": data1[key]
            })
        elif key in data2:
            diff.append({
                "key": key,
                "type": "added",
                "value": data2[key]
            })

    return diff
