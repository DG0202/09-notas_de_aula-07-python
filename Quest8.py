num = int(input("Digite seu número:"))
resultado = 1
i = 0

while i < num:
    i += 1
    resultado = resultado * i
print(f'O resultado do fatorial é {resultado}')