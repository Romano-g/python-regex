import re


cpf = '025.258.963-10'
cpf_regexp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')


ip_regexp = re.compile(r'''
    ^
        (?:
            (?:
                25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9]
            )
            \.?
        ){4}
    \b
    $
''', flags=re.X)


if __name__ == '__main__':
    # print(cpf_regexp.search(cpf))

    for i in range(301):
        ip = f'{i}.{i}.{i}.{i}'
        print(ip_regexp.findall(ip))
