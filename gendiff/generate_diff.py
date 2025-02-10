from gendiff.file_parser import load_file


def generate_diff(filepath1, filepath2):
    data1 = load_file(filepath1)
    data2 = load_file(filepath2)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        if key in data1 and key in data2 and data1[key] == data2[key]:
            diff.append(f"    {key}: {data1[key]}")
        elif key in data1 and key in data2 and data1[key] != data2[key]:
            diff.append(f"  - {key}: {data1[key]}")
            diff.append(f"  + {key}: {data2[key]}")
        elif key in data1:
            diff.append(f"  - {key}: {data1[key]}")
        elif key in data2:
            diff.append(f"  + {key}: {data2[key]}")

    return "{\n" + "\n".join(diff) + "\n}"
