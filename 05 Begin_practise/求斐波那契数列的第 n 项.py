x = eval(input('input x:'))
y = eval(input('input y:'))
z = eval(input('input z:'))
n = eval(input('input n:'))
z = x+y
for i in range(n-3):
    x = y
    y = z
    z = x+y
print(z)
