from itertools import groupby
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['simhei']
scores = {'数据结构': [89, 70, 49, 87, 92, 84, 73, 71, 78, 81, 90, 37, 77, 82, 81, 79, 80, 82, 75, 90, 54, 80, 70, 68, 61],
          '线性代数': [70, 74, 80, 60, 50, 87, 68, 77, 95, 80, 79, 74, 69, 64, 82, 81, 78, 90, 78, 79, 72, 69, 45, 70, 70],
          '英语': [83, 87, 69, 55, 80, 89, 96, 81, 83, 90, 54, 70, 79, 66, 85, 82, 88, 76, 60, 80, 75, 83, 75, 70, 20],
          'Python': [90, 60, 82, 79, 88, 92, 85, 87, 89, 71, 45, 50, 80, 81, 87, 93, 80, 70, 68, 65, 85, 89, 80, 72, 75]}


def splitScore(score):
    if score >= 85:
        return '优'
    elif score >= 60:
        return '及格'
    else:
        return '不及格'


rations = dict()
for subject, subjectScore in scores.items():
    rations[subject] = {}
    for category, num in groupby(sorted(subjectScore), splitScore):
        rations[subject][category] = len(tuple(num))

fig, axs = plt.subplots(2, 2)
axs.shape = 1, 4
for index, subjectData in enumerate(rations.items()):
    plt.sca(axs[0][index])
    subjectName, subjectRatio = subjectData
    plt.pie(list(subjectRatio.values()), labels=list(
        subjectRatio.keys()), autopct='%1.1f%%')
    plt.xlabel(subjectName)
    plt.legend()
plt.show()
