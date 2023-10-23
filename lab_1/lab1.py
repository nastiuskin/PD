x = int(input("Input a number in range 1 - 9: "))

if 1 <= x <= 3:
    s = input("Input a string : ")
    n = int(input("Input the amount of string repeats: "))
    for i in range(n):
        print(s)
elif 4 <= x <= 6:
    m = int(input("Enter the power to which the number should be raised: "))
    result = x ** m
    print("Result: " + str(result))
elif 7 <= x <= 9:
    for i in range(1, 11):
        x += 1
        print(x)
else:
    print("Input error")

print("Wekcome to program 'Society in the 21st Century'")

age = int(input("Enter your age: "))

if 0 <= age <= 7:
    print("You should go to a daycare.")
elif 7 < age <= 18:
    print("You should go to school.")
elif 18 < age <= 25:
    print("You should attend a higher educational institution.")
elif 25 < age <= 60:
    print("It's time to get a job.")
elif 60 < age <= 120:
    print("The choice is yours.")
else:
    print("Error! This program is for humans!")

