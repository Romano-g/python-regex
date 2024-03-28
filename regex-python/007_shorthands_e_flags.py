'''
flags:

re.I => Ignorecase, lê tanto minuscula quanto maiúscula
re.A => Ascii, pega só as letras padrão ascii
re.M => Multiline, faz com que ^ e $ sejam aplicados em todas linhas, e não
        somente no inicio e final do objeto
re.S => Dotall, faz com que leia as quebras de linha
'''

# shorthands:

# \w => Lê tudo, mesmo resultado que [a-zA-Z0-9À-ú]
# \W => Só acha pontuação, mesmo resulado que [^a-zA-Z0-9À-ú]
# \d => Lê numerações, mesmo resultado que [0-9]
# \D => Ignora numerações, mesmo resultado que [^0-9]
# \s => Lê todos os espaços, mesmo resultado que [ \r\n\f\t]
# \S => Ignora todos os espaços, mesmo resultado que [^ \r\n\f\t]
# \b => Encontra uma string no início ou fim da palavra (nas "bordas")
# \B => Encontra uma string no meio da palavra
