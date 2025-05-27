user_input = int(input("Enter the size of the pattern: "))

i = 1

while (i < user_input+1):
    for r in range(user_input + 1):
        print("*", end="")
    print()
    i += 1
