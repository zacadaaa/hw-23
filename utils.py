def build_query(cmd, value, data):
    if cmd == 'filter':
        result = filter(lambda item: value in item, data)
        return result

    if cmd == 'unique':
        result = list(set(data))
        return result

    if cmd == 'limit':
        value = int(value)
        result = list(data)[:value]
        return result

    if cmd == 'sort':
        reverse = value == 'desc'
        result = sorted(data, reverse=reverse)
        return result

    if cmd == 'map':
        value = int(value)
        result = map(lambda item: item.split(' ')[value], data)
        return result
