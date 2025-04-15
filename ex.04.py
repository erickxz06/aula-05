alunos = int(input("Digite a quantidade de alunos: "))
x = 0
soma = 0
while x <alunos:
    nota = float(input("Digite as notas dos alunos: "))
    x+=1
    soma = soma + nota
media = soma/alunos
print(media)

