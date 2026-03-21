'''
A documentação do Python pode ser acessada através do link:
https://docs.python.org/pt-br/3/library/stdtypes.html
Tipos Built-in são itens que já vem instalados com o Python
Os já visto até agora foram: str, int, float, bool
Esses são imutáveis (não é possivel muda-los ao decorrer do código)
'''
# EX:
string = 'lucas'
string[3] = 'ABC'
print(string[3])
'''
- Esse código vai apresentar um erro, pois string é uma variavel imutável
- Isso quer dizer que não é possivel mudar o valor atribuido a ela
- O que o código acima tentou fazer foi, tentar atribuir o valor 'ABC' no 
terceiro indice, que contém a letra 'a', porém como a string é imutável, ela 
não irá permitir que isso ocorra e apresentara um erro.
'''