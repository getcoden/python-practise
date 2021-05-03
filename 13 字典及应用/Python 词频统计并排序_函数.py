def WordCount(str):
    str = str.lower()
   
    # 删除标点符号等
    allchar = 'qwertyuiopasdfghjklzxcvbnm '
    for i in str:
        if i not in allchar:
            str = str.replace(i,'')

    word_list = str.split(' ')

    count_dict = {}
    # 如果字典里有该单词则加1，否则添加入字典
    for word in word_list:
        #中间有可能出现连续空格的情况，这样导致word_list中有可能含有''（空字符）
        #word_list中的空字符不统计
        if len(word) == 0:
            continue
        else:
            if word in count_dict.keys():
                count_dict[word] = count_dict[word] + 1
            else:
                count_dict[word] = 1
    count_list = sorted(count_dict.items(), key = lambda x: x[1], reverse = True)
    return count_list

print(WordCount('kdkk2563*/-'))