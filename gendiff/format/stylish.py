def stringify(value, depth):
    if isinstance(value, dict):
        indent = ' ' * (depth * 4)
        closing_indent = ' ' * ((depth - 1) * 4)
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}{k}: {stringify(v, depth + 1)}")
        return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)


def format_stylish(diff, depth=1):
    indent_for_unchanged = ' ' * (depth * 4)
    indent_for_marker = ' ' * (depth * 4 - 2)
    bracket_indent = ' ' * ((depth - 1) * 4)
    lines = []

    for item in diff:
        key = item["key"]
        typ = item["type"]

        if typ == "nested":
            nested = format_stylish(item["children"], depth + 1)
            lines.append(f"{indent_for_unchanged}{key}: {nested}")

        elif typ == "unchanged":
            value = stringify(item["value"], depth + 1)
            lines.append(f"{indent_for_unchanged}{key}: {value}")

        elif typ == "changed":
            old_value = stringify(item["old_value"], depth + 1)
            new_value = stringify(item["new_value"], depth + 1)
            line_old = (
                f"{indent_for_marker}- {key}:"
                if old_value == ""
                else f"{indent_for_marker}- {key}: {old_value}"
            )
            line_new = (
                f"{indent_for_marker}+ {key}:"
                if new_value == ""
                else f"{indent_for_marker}+ {key}: {new_value}"
            )
            lines.append(line_old)
            lines.append(line_new)

        elif typ == "removed":
            value = stringify(item["value"], depth + 1)
            line_removed = (
                f"{indent_for_marker}- {key}:"
                if value == ""
                else f"{indent_for_marker}- {key}: {value}"
            )
            lines.append(line_removed)

        elif typ == "added":
            value = stringify(item["value"], depth + 1)
            line_added = (
                f"{indent_for_marker}+ {key}:"
                if value == ""
                else f"{indent_for_marker}+ {key}: {value}"
            )
            lines.append(line_added)

    return "\n".join(["{"] + lines + [f"{bracket_indent}}}"])
