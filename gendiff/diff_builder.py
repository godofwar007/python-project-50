def build_diff(data1, data2):
    keys = sorted(set(data1) | set(data2))
    diff = []

    for key in keys:
        if key not in data1:
            diff.append({
                "key": key,
                "type": "added",
                "value": data2[key]
            })
            continue

        if key not in data2:
            diff.append({
                "key": key,
                "type": "removed",
                "value": data1[key]
            })
            continue

        value1 = data1[key]
        value2 = data2[key]

        if isinstance(value1, dict) and isinstance(value2, dict):
            diff.append({
                "key": key,
                "type": "nested",
                "children": build_diff(value1, value2)
            })
            continue

        if value1 == value2:
            diff.append({
                "key": key,
                "type": "unchanged",
                "value": value1
            })
            continue

        diff.append({
            "key": key,
            "type": "changed",
            "old_value": value1,
            "new_value": value2
        })

    return diff
