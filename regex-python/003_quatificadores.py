import re

'''
* => 0 ou N
+ => 1 ou N
? => 0 ou 1
{} => {n} ou {min, max}
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
jã
'''


if __name__ == '__main__':
    print(f'\n{re.findall(r"Jo+ão+", texto, flags=re.I)}')
    print(f'\n{re.findall(r"Jo*ão*", texto, flags=re.I)}')
    print(f'\n{re.findall(r"Jo?ão*", texto, flags=re.I)}')
    print(f'\n{re.findall(r"Jo{1,}ão", texto, flags=re.I)}')
