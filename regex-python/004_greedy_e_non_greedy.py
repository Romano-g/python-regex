import re

'''
* => 0 ou N
+ => 1 ou N
? => 0 ou 1
{} => {n} ou {min, max}
'''

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>
'''


if __name__ == '__main__':
    print(re.findall(r'<[divp]{1,3}>.*<\/[divp]{1,3}>', texto))
    print(re.findall(r'<[divp]{1,3}>.*?<\/[divp]{1,3}>', texto))
