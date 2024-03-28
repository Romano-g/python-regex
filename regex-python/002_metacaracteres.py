import re

'''
| => Ou
. => Qualquer caractere(exceto quebra de linha)
[] => Conjunto de caracteres
'''

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''


if __name__ == '__main__':
    print(re.findall(r'João|Maria|adultos', texto))
    print(f'\n{re.findall(r"João|Maria|ad.....", texto)}')
    print(f'\n{re.findall(r"[Jj]oão|[Mm]aria|adultos", texto)}')
    print(f'\n{re.findall(r"[a-zA-Z0-9]aria", texto)}')
    print(f'\n{re.findall(r"MariA", texto, flags=re.I)}')
