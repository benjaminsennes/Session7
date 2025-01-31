s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)
print(s1, "World")
print(3*s2)
print((10//2)*s1) # 10/2 = 5.0 and it' not an integer. We need either to divide by // or add int()
print(s1, len(s1)) # len() function gives you the size of the string
print(3*s2, len(3*s2))

for c in s2:
    print(c)

for c in s1:
    print(4*c, end="")

new_string = ""
for c in s2:
    new_string += c*4 # same as: new_string = new_string + 4 * c
print(new_string)

# it can be used to check if one string is inside another
print("H" in s1) # True
print("d" in s2) # True
print("x" in s1) # False
print("Wor" in s2) # True


