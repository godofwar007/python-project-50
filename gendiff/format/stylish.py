def stringify(value, depth):
    """Преобразует значение в строку с учётом вложенных структур."""
    if isinstance(value, dict):
        indent = ' ' * (depth * 4)
        closing_indent = ' ' * ((depth - 1) * 4)
        lines = [
            f"{indent}{k}: {stringify(v, depth + 1)}" for k, v in value.items()]
        return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"

    if value is None:
        return "null"

    if isinstance(value, bool):
        return str(value).lower()

    if value == "":  # Убираем кавычки для пустых строк
        return ""

    return str(value)


def format_stylish(diff, depth=1):
    indent = ' ' * (depth * 4)
    marker_indent = ' ' * (depth * 4 - 2)
    bracket_indent = ' ' * ((depth - 1) * 4)
    lines = []

    for item in diff:
        key = item["key"]
        typ = item["type"]

        if typ == "nested":
            children = format_stylish(item["children"], depth + 1)
            lines.append(f"{indent}{key}: {children}")

        elif typ == "unchanged":
            value = item["value"]
            val_str = stringify(value, depth + 1)
            lines.append(f"{indent}{key}: {val_str}")

        elif typ == "changed":
            old_value = item["old_value"]
            new_value = item["new_value"]
            old_str = stringify(old_value, depth + 1)
            new_str = stringify(new_value, depth + 1)
            if isinstance(old_value, dict):
                lines.append(f"{marker_indent}- {key}:\n{old_str}")
            else:
                lines.append(f"{marker_indent}- {key}: {old_str}")
            if isinstance(new_value, dict):
                lines.append(f"{marker_indent}+ {key}:\n{new_str}")
            else:
                lines.append(f"{marker_indent}+ {key}: {new_str}")

        elif typ == "removed":
            value = item["value"]
            val_str = stringify(value, depth + 1)
            if isinstance(value, dict):
                lines.append(f"{marker_indent}- {key}:\n{val_str}")
            else:
                lines.append(f"{marker_indent}- {key}: {val_str}")

        elif typ == "added":
            value = item["value"]
            val_str = stringify(value, depth + 1)
            if isinstance(value, dict):
                lines.append(f"{marker_indent}+ {key}:\n{val_str}")
            else:
                lines.append(f"{marker_indent}+ {key}: {val_str}")

    return "\n".join(["{"] + lines + [f"{bracket_indent}}}"])
