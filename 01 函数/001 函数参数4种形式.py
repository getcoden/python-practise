1 λ�ò���


2 �ؼ��ֲ���



3 ȱʡ�������ֽ�Ĭ�ϲ���

def func(name,age,male = '��'����
    
    pass


4 ����������

��1�����λ�ò����б��Ͳ� ����ֵΪԪ����ʽ����



��2���ֵ��Ͳ�  ����ֵΪ�ֵ�
def myfun(**kwargs):
    print('��������:',len(kwargs))
    for k,v in kwargs.items():
        print(k,'->>',v)
    print(kwargs)

myfun(name='midu',age=15,sex='male')