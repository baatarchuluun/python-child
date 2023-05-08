# simple calculator
print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Remainder")
print("6. Ceil")
s = int(input("Enter choose(1-6)"))
if (s < 1 or s > 6):
    print("Error")
else:
    n1 = int(input("1st number="))
    n2 = int(input("2nd number="))
    if s == 1:
        answer = n1 + n2
        print("{} + {} = {}".format(n1, n2, answer))
    elif s == 2:
        answer = n1 - n2
        print("{} - {} = {}".format(n1, n2, answer))
    elif s == 3:
        answer = n1 * n2
        print("{} * {} = {}".format(n1, n2, answer))
    elif s == 4:
        answer = n1 / n2
        print("{} / {} = {}".format(n1, n2, answer))
    elif s == 5:
        answer = n1 % n2
        print("{} % {} = {}".format(n1, n2, answer))
    else:
        answer = n1 // n2
        print("{} // {} = {}".format(n1, n2, answer))   