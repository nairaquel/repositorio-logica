import os
os.system("clear||cls")


nota = int(input("Digite sua nota: "))

while True:
    if nota < 0 or nota > 10:
        nota = int(input("Digite sua nota: "))
    else:
        break

print(f"Nota: {nota}\n")
print("FIM")