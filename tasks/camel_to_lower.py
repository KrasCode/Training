"""
 написать функцию, которая будет переводить CamelCase в Lowercase с подчеркиванием
"""


def find_index(name: str) -> int:
    for pos in range(1, len(name)):
        if name[pos].isupper():
            return pos
    return 0


def transform(name: str) -> str:
    new_name = name.lower()
    place = find_index(name)
    if place == 0:
        return new_name
    else:
        return new_name[:place] + '_' + new_name[place:]


if __name__ == '__main__':
    print(transform('HelloWorld'))
