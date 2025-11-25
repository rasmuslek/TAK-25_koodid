name = str(input("Mis on sinu nimi?: "))
print("Tere", name)
place = str(input("Mis on sinu elukoht?: "))
if place == "saaremaa":
    print("Kas sa teatsid, et Ott Tänak käis Kuressaare Ametikoolis?")
age = int(input("Kui vana sa oled?: "))
if age == 18:
    print("Head 18 sünnipäeva:")
if age < 18:
    print("Sa oled liiga noor, et autoga sõita")
if age > 18:
    print("Sa võid autoga sõita")
