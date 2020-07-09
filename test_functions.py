
def max_for_dicts(elements, key):
    if not elements:
        return

    max_key = elements[0][key]
    max_element = elements[0]

    for element in elements:
        if element[key] > max_key:
            max_key = element[key]
            max_element = element

    return max_element


def filter_dicts(elements, key, min_value):
    new_elements = []

    for element in elements:
        if element[key] >= min_value:
            new_elements.append(element)

    return new_elements
