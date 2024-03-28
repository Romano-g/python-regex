import re


regex = re.compile(
    r'^(?:\(\d{2}\)\s*)(?:9\s*)(?:\d{4}-\d{4})$', flags=re.M
)


texto = '''
(21) 9 8852-5214
(11)9955-1231
(11)            9955-1231
(35) 9 9975-4521
(31) 3851-2587
9 8571-5213
1234-5647
'''


if __name__ == '__main__':
    for telefone in regex.findall(texto):
        print(telefone)
