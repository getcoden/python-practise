def file_replace(file_name, re_word, ne_word):
    f_read = open(file_name)
    content = []
    count = 0
    for eachword in f_read:
        if re_word in eachword:
            count += 1
            eachword = eachword.replace(re_word, ne_word)
        content.append(eachword)
    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：'
                   % (file_name, count, re_word, re_word, ne_word))
    if decide in ['YES', 'Yes', 'yes']:
        f_write = open(file_name, 'w')
        f_write.writelines(content)
        f_write.close()

    f_read.close()


file_name = input('请输入文件名：')
re_word = input('请输入需要替换的单词或字符：')
ne_word = input('请输入新的单词或字符：')
file_replace(file_name, re_word, ne_word)
