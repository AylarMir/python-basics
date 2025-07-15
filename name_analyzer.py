name = input("Enter your name: ")

# Basic stats
print("-" * 30)
print(f"Length: {len(name)}")
print(f"Upper : {name.upper()}")
print(f"Lower : {name.lower()}")
print("-" * 30)

# Check first letter, case-insensitive
if name[0].upper() == "A":
    print("Your name starts with the letter A")
else:
    print("Your name doesn’t start with A")

# Special nickname for Aylar
if name.lower() == "aylar":
    nickname = "The Moon"
    print(f"New Nickname: {nickname}")