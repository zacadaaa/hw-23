import re

from typing import Iterable, Any, List


def build_query(cmd: str, value: str, data: Iterable) -> List[Any]:
    if cmd == 'filter':
        result = list(filter(lambda item: value in item, data))
        return result

    if cmd == 'unique':
        result = list(set(data))
        return result

    if cmd == 'limit':
        result = list(data)[:int(value)]
        return result

    if cmd == 'sort':
        reverse = value == 'desc'
        result = list(sorted(data, reverse=reverse))
        return result

    if cmd == 'map':
        result = list(map(lambda item: item.split(' ')[int(value)], data))
        return result

    if cmd == 'regex':
        regex = re.compile(value)
        result = list(filter(lambda x: regex.search(x), data))
        return result
