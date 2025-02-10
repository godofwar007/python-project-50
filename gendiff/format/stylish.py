def format_stylish(diff, depth=1):
    def get_indent(depth):
        return ' ' * (depth * 4 - 2)

    def render_line(prefix, key, value, depth):

        formatted_value = format_value(value, depth + 1)
        if formatted_value == "":
            return f"{prefix}{key}:"
        return f"{prefix}{key}: {formatted_value}"

    current_indent = get_indent(depth)
    bracket_indent = ' ' * ((depth - 1) * 4)
    lines = []

    for item in diff:
        key = item['key']
        typ = item['type']
        if typ == 'nested':
            lines.append(
                f"{current_indent}  {key}: "
                f"{format_stylish(item['children'], depth + 1)}")
        elif typ == 'unchanged':
            lines.append(
                f"{current_indent}  {key}: "
                f"{format_value(item['value'], depth + 1)}")
        elif typ == 'changed':
            lines.append(render_line(current_indent + "- ",
                         key, item['old_value'], depth))
            lines.append(render_line(current_indent + "+ ",
                         key, item['new_value'], depth))
        elif typ == 'removed':
            lines.append(render_line(current_indent +
                         "- ", key, item['value'], depth))
        elif typ == 'added':
            lines.append(render_line(current_indent +
                         "+ ", key, item['value'], depth))

    result = "\n".join(["{"] + lines + [f"{bracket_indent}}}"])
    return result


def format_value(value, depth):

    if isinstance(value, dict):
        indent = ' ' * (depth * 4)
        bracket_indent = ' ' * ((depth - 1) * 4)
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}{k}: {format_value(v, depth + 1)}")
        return "\n".join(["{"] + lines + [f"{bracket_indent}}}"])
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)
