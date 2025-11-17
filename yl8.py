n1 = float(input("Sisesta aasta: "))
if (n1 % 400 == 0) or (n1 % 4 == 0) and not (n1 % 100 == 0):
    print(n1, "on liigaasta")
else:
    print(n1, "on lihtaasta")   