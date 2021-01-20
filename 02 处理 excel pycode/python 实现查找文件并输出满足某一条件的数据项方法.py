"""
python 实现查找文件并输出满足某一条件的数据项方法

"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 1 12:24:18 2018

版本1

@author: Administrator
"""

def main():
  file=open("students.txt",'r') 
  lines=file.readlines() #使用readlines()函数 读取文件的全部内容，存成一个列表，每一项都是以换行符结尾的一个字符串，对应着文件的一行

  list_name=[] #初始化一个空列表 用来存该文件的姓名 也就是第一列
  list_scores=[]
  list_gpa=[]

  for line in lines:   #开始进行处理 把第一列存到list_name 第二列存到list_scores,,,,,
    elements=line.split()
    list_name.append(elements[0])
    list_scores.append(elements[1])
    list_gpa.append(elements[2])

  max_gpa=0 
  index=0

  for i in range (len(list_gpa)):  #对于列表list_gpa 遍历该列表找其中gpa分数最高的
    if max_gpa <float(list_gpa[i]):
      max_gpa=float(list_gpa[i])
      index=i      #这一步就是记录list_gpa中GPA最高的在列表的第几个位置，方面输出对应的姓名和分数
  print("the person is {0} and the scores are {1} ,the gpa is {2}".format(list_name[index],list_scores[index],max_gpa))

main()

"""
版本2

"""

#这个是根据第二项hours和第三项points的比值，哪个值大就输出对应的学分points和GPA值points/hours

def main():
  file=open("students.txt",'r')
  lines=file.readlines()
  list_name=[]
  list_hours=[]
  list_points=[]

  for line in lines:
    elements=line.split()
    list_name.append(elements[0])
    list_hours.append(elements[1])
    list_points.append(elements[2])

  list_gpa=[] #这个列表用来存放hours 和points之间的比值

  for i in range(len(list_name)):
    a=float(list_hours[i])
    b=float(list_points[i])
    c=b/a
    list_gpa.append(str(c))  #把原来list_hours 和list_points中对应项的比值都存到list_gpa列表中

  maxgpa=0
  for i in range(len(list_gpa)):  #找list_gpa中值最大的那项
    if maxgpa<float(list_gpa[i]):
      maxgpa=float(list_gpa[i])
      index=i  #记录下gpa值最大的那项对应的索引值，方便输出其他项
  print("the max GPA is {},his name is {} and the scorespoint is {}".format(maxgpa,list_name[index],list_points[index]))

main()
