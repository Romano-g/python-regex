import re


string = 'Este é um teste de expressões teste regulares.'

# print(re.search(r'teste', string))
# print(re.findall(r'teste', string))
# print(re.sub(r'teste', 'abc', string))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(f"\n{regexp.findall(string)}")
print(f"\n{regexp.sub('def', string)}")
print(f"\n{regexp.sub('def', string, count=1)}")
