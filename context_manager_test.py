'''
name = open("data.txt", "r")

chk = name.readable()
if chk:
    print(name.read())
else:
    print("Can't read the file.")

print(name.readline(), end="")
print(name.readline(), end="")


i = 1
for line in name:
    print(f"Line {i}: {line}", end="")
    i += 1

name.close()
'''
#----------------------------------------

'''
file = open("output.txt", "w")
file.write("Hello Aylar\nYou're learning Python\nAnd it's going great!")
file.close()

change = open("output.txt", "a")
change.write("\nYou're becoming a real dev!")
change.close()
new = open("output.txt", "r")
print(new.read())
new.close()
'''
#----------------------------------------

import my_module
print(my_module.name)
print(my_module.say_hello())