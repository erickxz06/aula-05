senha = int(input("Digite a senha: "))
pin = 1234
tentativas = 1

while senha != pin and tentativas<3:
    senha = int(input("Digite a senha novamente: "))
    tentativas = tentativas+1
if senha == pin:
    print("Senha correta")
else:
    print("Acesso bloqueado")





