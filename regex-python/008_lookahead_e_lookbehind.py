from pprint import pprint
import re


texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''


if __name__ == '__main__':
    # Positive lookahead
    # pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))
    # pprint(re.findall(r'(?=.*[^in]active).+', texto))

    # Negative lookahead
    # pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))

    # Positive lookbehind
    # pprint(
    #     re.findall(
    #         r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+',
    #         texto))

    # Negative lookbehind
    pprint(
        re.findall(
            r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+',
            texto))
