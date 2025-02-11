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
            lines.append(
                f"{indent_for_unchanged}{key}: " + (value if value else "")
            )

        elif typ == "changed":
            old_value = stringify(item["old_value"], depth + 1)
            new_value = stringify(item["new_value"], depth + 1)

            lines.append(
                f"{indent_for_marker}- {key}: " +
                (old_value if old_value else "")
            )
            lines.append(
                f"{indent_for_marker}+ {key}: " +
                (new_value if new_value else "")
            )

        elif typ == "removed":
            value = stringify(item["value"], depth + 1)
            lines.append(
                f"{indent_for_marker}- {key}: " + (value if value else "")
            )

        elif typ == "added":
            value = stringify(item["value"], depth + 1)
            lines.append(
                f"{indent_for_marker}+ {key}: " + (value if value else "")
            )

    return "\n".join(["{"] + lines + [f"{bracket_indent}}}"])
