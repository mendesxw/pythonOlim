H = int(input())
M = int(input())
S = int(input())
T = int(input())

total_segundos_originais = H * 3600 + M * 60 + S

total_segundos_adiados = total_segundos_originais + T

novo_H = (total_segundos_adiados // 3600) % 24
novo_M = (total_segundos_adiados % 3600) // 60
novo_S = total_segundos_adiados % 60

print(novo_H)
print(novo_M)
print(novo_S)