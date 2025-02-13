NESTED = "nested"
UNCHANGED = "unchanged"
ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"


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
            change_type = item["type"]

            if change_type == NESTED:
                lines.extend(iter_plain(item["children"], full_key))
            elif change_type == UNCHANGED:
                continue
            elif change_type == ADDED:
                value = stringify(item["value"])
                lines.append(
                    f"Property '{full_key}' was added with value: {value}"
                )
            elif change_type == REMOVED:
                lines.append(f"Property '{full_key}' was removed")
            elif change_type == CHANGED:
                old_val = stringify(item["old_value"])
                new_val = stringify(item["new_value"])
                lines.append(
                    f"Property '{full_key}' was updated. "
                    f"From {old_val} to {new_val}"
                )
        return lines

    return "\n".join(iter_plain(diff))
