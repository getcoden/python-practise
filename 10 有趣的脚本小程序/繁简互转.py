# 3 实例：
import opencc
# 第一步打开文本文件，for 读取每句繁体
with open(r"C:\Users\win\Desktop\t.txt", 'r') as f:
    question_labels = f.readlines()

q_zh = []  # Data中问题的中文
for line in question_labels:
    line = line.strip('\n')
    q_zh.append(line)

print(q_zh)
# ['請問京都議定書規定幾個工業國家的二氧化碳排放量限制？', '請問首位自費太空旅行的觀光客為誰？',]

# 第二步转换


def Traditional2Simplified(sentence):

    cc = opencc.OpenCC('t2s')
    sentence = cc.convert(sentence)
    return sentence


q_zh_jian = []
for line in q_zh:
    q_zh_jian.append(Traditional2Simplified(line))
with open(r"C:\Users\win\Desktop\t2s.txt", 'a') as w:
    for wr in q_zh_jian:
        w.write(wr+'\n')
