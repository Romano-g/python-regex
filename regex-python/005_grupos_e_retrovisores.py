import re
'''
() => Tem que encontrar especificamente o grupo que as () contém
'''

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>
'''

cpf = 'a 147.852.963-12 a'

if __name__ == '__main__':
    print(re.findall(r'<(?P<tag>[divp]{1,3})>(.*?)<\/(?P=tag)>', texto))

    print(re.findall(r'(?:[0-9]{3}\.){2}[0-9]{3}\-[0-9]{2}', cpf))

    print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4', texto))
