import re
'''
^ => Começa com
$ => Termina com
[^a-z] => Negação
'''


cpf = '147.852.963-12'

if __name__ == '__main__':
    print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}\-[0-9]{2})$', cpf))
    print(re.findall(r'[^a-z]+', cpf))
