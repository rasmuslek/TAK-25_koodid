fruit = ["õun", "Pirn", "Mango"]
print(fruit[0])
fruit.append("Arbuus")
print(fruit[-1])
fruit[1] = "Banaan"
print(fruit)
if "õun" in fruit:
    print("Õun on listis")
else:
    print("Õun ei ole listis")
print(len(fruit))
fruit.remove("Mango")
fruit.reverse()
print(fruit)