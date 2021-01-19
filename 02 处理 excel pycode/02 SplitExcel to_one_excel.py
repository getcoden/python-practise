
import pandas as pd
import os


data = pd.read_excel('./���꼶�˺ź�����.xls')#��ȡ����
data_list = list(data['�༶'].drop_duplicates())#ȥ�ش���
longth = len(data_list)#���㹲�ж�������
path = './SplitExcel'
if not os.path.exists(path):#��ǰ�ļ������Ƿ��д��ļ���
    os.mkdir(path)#�������ļ���
count = 0
for item in data_list:
    data_select = data[data['�༶']==item]#ѡ��item��Ӧ����
    Bigzone = data_select.iat[0,0]#��Ҫ�����ļ�������ֵ
    Smallzone = data_select.iat[0,1]
    service_code = data_select.iat[0,2]
    data_select.to_excel('./SplitExcel/{0:}-{1:}.xlsx'.format(Bigzone,Smallzone),index=False)#���ն�Ӧ��ֵ����EXCEL�ļ�
    count += 1
    print('\rEXCEL���й��� {} ���༶�����ڲ�ֵ� {} �������ݣ���ֽ��ȣ�{:.2%}'.format(longth, count, count / longth),end="")   
print('\n{}�������Ѿ�ȫ�������ϣ���ǰ��SplitExcel�ļ����²鿴��ֺ�ĸ��ļ�����.'.format(longth))
