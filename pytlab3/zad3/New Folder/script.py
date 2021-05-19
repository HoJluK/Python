from re import finditer


def script(filename):
    try:
        file = open(filename, "rt")
        for i, line in enumerate(file.buffer, 1):
            line = line.decode('utf-8')
            for match in finditer(r'\b?[0-1][0-9]-[0-5][0-9]-[0-5][0-9][0-5][0-9]\b?)', line):
                yield ("Строка {}, позиция {} : найдено '{}'"
                       .format(i, match.span()[0] + 1, match.group()))
    finally:
        file.close()
