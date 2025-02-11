def stringify(value, depth):
    if isinstance(value, dict):
        indent = ' ' * (depth * 4)
        closing_indent = ' ' * ((depth - 1) * 4)
        lines = [
            f"{indent}{k}: {stringify(v, depth + 1)}"
            for k, v in value.items()]
        return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)


def render_item(item, depth):
    indent_unchanged = ' ' * (depth * 4)
    indent_marker = ' ' * (depth * 4 - 2)
    key = item["key"]
    typ = item["type"]

    if typ == "nested":
        nested = format_stylish(item["children"], depth + 1)
        return f"{indent_unchanged}{key}: {nested}"
    if typ == "unchanged":
        value = stringify(item["value"], depth + 1)
        return f"{indent_unchanged}{key}: {value}"
    if typ == "changed":
        old_value = stringify(item["old_value"], depth + 1)
        new_value = stringify(item["new_value"], depth + 1)
        line1 = (
            f"{indent_marker}- {key}: {old_value}"
            if old_value != ""
            else f"{indent_marker}- {key}:"
        )
        line2 = (
            f"{indent_marker}+ {key}: {new_value}"
            if new_value != "" else f"{indent_marker}+ {key}:")
        return f"{line1}\n{line2}"
    if typ == "removed":
        value = stringify(item["value"], depth + 1)
        return (f"{indent_marker}- {key}: {value}"
                if value != "" else f"{indent_marker}- {key}:")
    if typ == "added":
        value = stringify(item["value"], depth + 1)
        return (
            f"{indent_marker}+ {key}: {value}"
            if value != "" else f"{indent_marker}+ {key}:")
    return ""


def format_stylish(diff, depth=1):
    bracket_indent = ' ' * ((depth - 1) * 4)
    lines = [render_item(item, depth) for item in diff]
    return "\n".join(["{"] + lines + [f"{bracket_indent}}}"])
