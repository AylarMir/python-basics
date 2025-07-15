#--------------- Raising a num to a power ---------------------
def power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

#--------------- For loop ---------------------
favAnimal = ["cat", "shark", "fox", "dog", "crow"]
count = 0
for animal in favAnimal:
    print(animal)
    if "a" in animal:
        count += 1
print(f"Number of animals with 'a': {count}")

#--------------- While loop ---------------------
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue  # skip the rest and jump to next loop
    print(i)
    i += 1

#-------------- 2D lists ---------------------
nums = [[3,4,5],[6,7,8],[9,0,1]]
print(nums[0][1])
print(nums[2][2])
print(f"Answer of {nums[0][0]} + {nums[2][2]} = " + str(nums[0][0]+nums[2][2]))

#-------------- Nested loops to output 0 1 2 ---------------------
for row in range(3):
    for col in range(3):
        print(f"{row}-{col}", end=" ")
    print()

#--------------- Or ---------------------
i = 0
while i < 3:
    for j in range(3):
        print(j, end=" ")
    print()
    i += 1

#--------------- Number searcher ---------------------
list1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

try:
    num = int(input("Enter a number: "))
    found = False
    
    for row in range(len(list1)):
        for col in range(len(list1[row])):
            if list1[row][col] == num:
                print(f"Number found at Row: {row}, Column: {col}")
                found = True
                
    if not found:
        print("Number not found in the list.")

except ValueError as error:
    print(f"Please enter a valid number. {error}")

#--------------- Try-except-as ---------------------
try:
    num1 = input("Enter the numerator: ")
    num2 = input("Enter the denominator: ")

    numerator = float(num1)
    denominator = float(num2)

    result = numerator / denominator
    print(f"The result is: {result}")

except (ValueError, ZeroDivisionError) as error:
    print(f"Oops! Something went wrong: {error}")