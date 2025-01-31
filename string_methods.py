print(dir("hello"))

print(help("hi".capitalize))
print("i like to go to school".capitalize())
print("IS THIS SUPPOSED TO WORK?".capitalize())

print("hello".center(50, "x"))
print("gmail.com".find("."))
print("gmail.com".find("John"))
s = "i see a cat who likes to cat while i cat on a cat"
# find all occurences
poz = 0
while True:
    poz = s.find("cat", poz)
    if poz == -1:
        break
    print("I found cat on position", poz)
    poz += 1

# join - we will come back later

# lower
s = " I SEE A LOT OF THINGS !"
print(s.lower())

# replace - replace x with y
s = " I see a cat who likes to eat a rat. what a good cat"
print(s.replace("c", "r"))
print(s.replace("cat", "lion"))
s = "Hello, kind sir! How are you today?"
print(s.replace(",","").replace("!","").replace("?",""))

# split
s = "I like to go shopping"
print(s.split())
splitted = s.split()
print("XX".join(splitted))

# title
s = "i like the mountains"
print(s.title())

# upper
s = "i see a lot of things !"
print(s.upper())


