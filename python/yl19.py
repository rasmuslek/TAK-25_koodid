text = str(input("Sisesta lause: "))
vowels = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
count = 0
for letter in text:
    if letter in vowels:
        count += 1

print("Täishäälikute arv on:", count)
