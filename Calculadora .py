op = input('escolha a operação(+,-,*,/):')
x = input('primeiro membro')
y = input('segundo membro')

soma = int(x) + int(y)
subitração = int(x) - int(y)
multiplicação = int(x) * int(y)
divisão= int(x) / int(y)

if op=='+':
    print(soma)
if op=='-':
    print(subitração)
if op=='*':
    print(multiplicação)
if op=='/':
    print(divisão)
