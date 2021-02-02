a = int(input('Please  enter a number(1st < 2nd): '))
b = int(input('please enter another number(1st < 2nd): '))

if a == 0:
    print(a * b)
elif b == 0:
    print(a * b)
else:
    if (a % b == 0):
        print(b)
    while (a % b != 0):
        z = a % b
        x = b % z
        if x == 0:
            print(z)
        else:
            print(x)
        break
