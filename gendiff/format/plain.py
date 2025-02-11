def stringify(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def format_plain(diff):
    def iter_plain(diff, ancestry=""):
        lines = []
        for item in diff:
            key = item["key"]
            full_key = f"{ancestry}.{key}" if ancestry else key
            typ = item["type"]

            if typ == "nested":
                lines.extend(iter_plain(item["children"], full_key))
            elif typ == "unchanged":
                continue
            elif typ == "added":
                value = stringify(item["value"])
                lines.append(
                    f"Property '{full_key}' was added with value: {value}")
            elif typ == "removed":
                lines.append(f"Property '{full_key}' was removed")
            elif typ == "changed":
                old_val = stringify(item["old_value"])
                new_val = stringify(item["new_value"])
                lines.append(
                    f"Property '{full_key}' was updated. "
                    f"From {old_val} to {new_val}"
                )
        return lines

    return "\n".join(iter_plain(diff))
