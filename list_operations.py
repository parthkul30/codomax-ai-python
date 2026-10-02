fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original list:", fruits)

fruits.append("Grapes")
print("After adding Grapes:", fruits)

fruits.remove("Banana")
print("After removing Banana:", fruits)

print("First fruit:", fruits[0])

print("All fruits:")

for fruit in fruits:
    print(fruit)
