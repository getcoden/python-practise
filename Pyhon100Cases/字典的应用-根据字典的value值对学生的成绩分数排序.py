'''当学生的分数是以“姓名”+“分数”存储在文本文档中时，将“姓名”存储为字典中的key值，“分数”存储为字典中的value值，通过比较value值的大小进行学生分数的排序。
例如下面三个学生：
张三 87.5
李四 92
王五 71
'''

def read(fileName):
    st = []
    f = open(fileName,'r',encoding='utf-8')
    rows = f.readlines()
    for row in rows:
        s = row.strip("\n").split(" ")
        if len(s)==2:
            d = {"Name":s[0],"Score":str(s[1])}
            st.append(d)
    return st

def sort(st):
    for i in range(len(st)):
        for j in range(i+1,len(st)):
            if st[i]["Score"] < st[j]["Score"]:
                temp = st[i]
                st[i] = st[j]
                st[j] = temp

    return st

def save(st):
    f = open(r"F:\123\python-practise\Pyhon100Cases\sorted.txt",'w')
    for s in st:
        f.write(s['Name']+" "+str(s["Score"])+"\n")
    #f.close

if __name__ == '__main__':

    fileName = r"F:\123\python-practise\Pyhon100Cases\marks.txt"
    st = read(fileName)
    st = sort(st)
    save(st)

