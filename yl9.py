n1 = float(input("Sisesta esimene Külg: "))
n2 = float(input("Sisesta teine külg: "))
n3 = float(input("Sisesta kolmas külg: "))
if (n1 <= 0) or (n2 <= 0) or (n3 <= 0):
    print ("Sisesta õiged arvud")
elif (n1 == n2) and (n2 == n3) and not (n1 <= 0) and not (n2 <= 0) and not (n3 <= 0):
    print("Sinu kolmnurk on võrdkülgne")
elif (n1 == n2) and not (n2 == n3) and not (n1 <= 0) and not (n2 <= 0) and not (n3 <= 0):
    print("Sinu kolmnurk on võrdhaarne")
elif not (n1 == n2) and not (n2 == n3) and not (n3 == n1) and not (n1 <= 0) and not (n2 <= 0) and not (n3 <= 0):
    print("Sinu kolmnurk on erikülgne")