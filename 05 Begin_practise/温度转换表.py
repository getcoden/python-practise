for a in range(1):
    a = int(input('如果是华氏转摄氏，请按1\n,如果是摄氏转华氏，请按2\n'))
if a == 1:
    h = float(input("请输入华氏温度"))
    s = (h*1.8)+32
    print("{}华氏度转是{}摄氏度".format(h, s))
else:
    a == 2
s1 = float(input("请输入摄氏温度"))
h1 = (s1-32)*5/9
print("{}摄氏度转是{}华氏度".format(s1, h1))
