'''
需要将YEAR_UNIT_DEPOSIT_PRO这一列的数据按照指定分隔符‘|’拆分为12列，并拼接到原始数据中生成新的dataframe。

方法如下：
'''
# 数据拆分、拼接
new_names = ['gjj_pro_' + str(x + 1) for x in range(12)] # 为新生成的列取名
gjj_pro = gjj_pboc['YEAR_UNIT_DEPOSIT_PRO'].str.split('|', expand=True) # 将数据按‘|’拆分
gjj_pro.columns = new_names # 重命名新生成的列名
gjj_pboc = gjj_pboc.join(gjj_pro) # 数据合并