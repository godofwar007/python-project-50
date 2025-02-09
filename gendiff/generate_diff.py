import json


def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def generate_diff(filepath1, filepath2):
    data1 = load_json(filepath1)
    data2 = load_json(filepath2)

    all_data = sorted(set(data1.keys()) | set(data2.keys()))

    diff = []
    for key in all_data:
        if key in data1 and key in data2 and data1[key] == data2[key]:
            diff.append(f"  {key}: {data1[key]}")
        elif key in data1 and key in data2 and data1[key] != data2[key]:
            diff.append(f"- {key}: {data1[key]}")
            diff.append(f"+ {key}: {data2[key]}")
        elif key in data1:
            diff.append(f"- {key}: {data1[key]}")
        elif key in data2:
            diff.append(f"+ {key}: {data2[key]}")

    return "{\n" + "\n".join(diff) + "\n}"
