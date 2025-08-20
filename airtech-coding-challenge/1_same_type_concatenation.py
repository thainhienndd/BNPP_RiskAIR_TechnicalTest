from typing import List, Any

# Function to concatenate list of same types
def same_type_concat(items: List[Any]):
    # cas où pas d'items
    if not items:
        return None

    # Function to retrieve type of each list element
    def kind(x):
        if isinstance(x, bool):
            return 'bool'
        if isinstance(x, (int, float)) and not isinstance(x, bool):
            return 'number'
        if isinstance(x, str):
            return 'str'
        if isinstance(x, list):
            return 'list'
        if isinstance(x, dict):
            return 'dict'
        return type(x).__name__

    # Get the list of kinds
    kinds = [kind(x) for x in items]
    first_kind = kinds[0]

    # Case when types within a list are different
    if any(k != first_kind for k in kinds):
        raise TypeError("Mixed types not allowed")

    # int/float: sum
    if first_kind == 'number':
        return sum(items)

    # str: join |
    if first_kind == 'str':
        return '|'.join(items)

    # Bool: 1 or 0
    if first_kind == 'bool':
        return ''.join('1' if x else '0' for x in items)

    # List: concat
    if first_kind == 'list':
        out = []
        for l in items:
            out.extend(l)
        return out

    # dict: concat --> If same key, replace key
    if first_kind == 'dict':
        res = {}
        for d in items:
            res.update(d)
        return res
    raise TypeError("Unsupported type")

print(f"Case str: {same_type_concat(['Hello', 'AIR', 'TECH'])}")
print(f"Case int/float: {same_type_concat([3, 1.4, 32])}")
print(f"Case bool: {same_type_concat([True, True, False, True])}")
print(f"Case list: {same_type_concat([[1, 2], [3, 3], ['2', '3']])}")
print(f"Case dict: {same_type_concat([{'1': 3}, {2: 'A'}, {'3': 44}])}")


