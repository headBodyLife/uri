grana = float(input())
cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
cont = 0
resto = 0
print("NOTAS:")
# 13:34

for cedula in cedulas:
	resto = int(grana / cedula) # 1
	print(f"{resto} nota(s) de R$ {cedulas[cont]:.2f}")
	cont+=1
	grana = grana % cedula # 50
print("MOEDAS:")
cont = 0
for moeda in moedas:
	resto = int(round(grana,2) / moeda) # 1
	print(f"{resto} moeda(s) de R$ {moedas[cont]:.2f}")
	cont+=1
	grana = grana % moeda # 50
