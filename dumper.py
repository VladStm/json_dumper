def dump(result, data, level : int) -> str:
    if isinstance(data, (int, float, str)):
        result += ('  ' * level) + str(data) + '\n'
    elif isinstance(data, list):
        for value in data:
            result = dump(result, value, level + 1)
    elif isinstance(data, dict):
        result += '\n'
        for key in data:
            result += '{}{}='.format('  ' * level, key)
            if isinstance(data[key], list) and not isinstance(data[key][0], dict):
                result += '\n'
            if isinstance(data[key], (int, float, str)):
                result = dump(result, data[key], 0)
            else:
                result = dump(result, data[key], level + 1)
    else:
        raise TypeError

    return result


if __name__ == '__main__':
    data = {
        "name": "Vlad",
        "surname": "Paterylo",
        "children": [
            {
                "name": "Leo",
                "surname": "Surname",
                "marks": [
                    5,
                    4,
                    3,
                    2,
                    1
                ]
            },
            {
                "name": "Jim",
                "surname": "wick",
                "marks": "No marks"
            }
        ],
        "Job": {
            "company": "Nocompany",
            "position": "Developer"
        }
    }

    result = dump('', data, 0)
    print(result.strip())
