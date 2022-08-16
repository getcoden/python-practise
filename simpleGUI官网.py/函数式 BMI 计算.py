print('中国 BMI 指数')
print('偏瘦 <=18.4')
print('正常 18.5 ~ 23.9')
print('过重 24.0 ~ 27.9')
print('肥胖 >= 28.0')
height = float(input('请输入您的身高(米):'))
print('您的身高: ', height)
weight = float(input('请输入您的体重(千克):'))
print('您的体重: ', weight*2)
bmi = weight / (height) ** 2
print('您的 BMI 指数: ', bmi)
if bmi <= 18.4:
    print('您的体重过轻 @_@')
    print('偏瘦')
if 18.5 <= bmi <= 23.9:
    print('您的体重正常 @_@')
    print('正常')
if 24.0 <= bmi <= 27.9:
    print('您的体重过重 @_@')
    print('过重')
if 29.9 <= bmi:
    print('要减肥了 @_@')
