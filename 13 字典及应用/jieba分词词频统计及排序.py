import jieba

# txt="我是中国人，我爱中国。中国位于亚洲。"
# fenci = jieba.lcut(txt)
# d = {}
# for c in fenci:
# 	d[c] = d.get(c, 0) + 1
# print(d)
'''
d.get(c,0)的功能是：返回字典d中，键为c的元素的对应值，如果目前没有键为c的元素，则返回0。

如果不想要标点符号或一些停用词，可以在循环里加判断来筛选。如果停用词比较多，可以搜停用词表。
'''

# 接下来再把字典转换为属性的列表即可。

# 方法1（不排序）：

# m = list(d.items())
# m.sort(key=lambda x: x[1], reverse=True)
# print(m)

'''
这里使用了匿名函数的方法。

匿名函数的格式是：  lambda 参数:表达式，这样写比def来的更简单。

例如，要实现两个数相乘：'''
# def f(x, y):
# 	return x * y
# print(f(3, 4))

#匿名函数

func=lambda x,y:x*y
print(func(3,4))