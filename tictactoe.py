tabuleiro = [
[0,0,0],
[0,0,0],
[0,0,0]
]
for i in tabuleiro:
print(i)
linha = int(input("Digite o número da linha : "))
coluna = int(input("Digite o número da coluna : "))
if linha == 0 and coluna == 0:
tabuleiro[0][0] = "x"
elif linha == 0 and coluna == 1:
tabuleiro[0][1] = "x"
elif linha == 0 and coluna == 2:
tabuleiro[0][2] = "x"
elif linha == 1 and coluna == 0:
tabuleiro[1][0] = "x"
elif linha == 1 and coluna == 1:
tabuleiro[1][1] = "x"
elif linha == 1 and coluna == 2:
tabuleiro[1][2] = "x"
elif linha == 2 and coluna == 0:
tabuleiro[2][0] = "x"
elif linha == 2 and coluna == 1:
tabuleiro[2][1] = "x"
elif linha == 2 and coluna == 2:
tabuleiro[2][2] = "x"
for i in range(1):
linha = int(input("Digite o número da linha : "))
coluna = int(input("Digite o número da coluna : "))
if linha == 0 and coluna == 0:
tabuleiro[0][0] = "o"
elif linha == 0 and coluna == 1:
tabuleiro[0][1] = "o"
elif linha == 0 and coluna == 2:
tabuleiro[0][2] = "o"
elif linha == 1 and coluna == 0:
tabuleiro[1][0] = "o"
elif linha == 1 and coluna == 1:
tabuleiro[1][1] = "o"
elif linha == 1 and coluna == 2:
tabuleiro[1][2] = "o"
elif linha == 2 and coluna == 0:
tabuleiro[2][0] = "o"
elif linha == 2 and coluna == 1:
tabuleiro[2][1] = "o"
elif linha == 2 and coluna == 2:
tabuleiro[2][2] = "o"
else:
print(i)
for i in tabuleiro:
print(i)
