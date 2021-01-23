from faker import Faker
import xlwt
import pandas as pd

fake = Faker('zh_CN')


def save_to_excel(save_name, save_path, n):
    work_book = xlwt.Workbook(encoding='utf-8')
    work_sheet = work_book.add_sheet(save_name)

    # 添加字段名
    head = ['姓名', '性别', '身份证号', '出生日期', '手机号', '家庭地址']
    for h in range(len(head)):
        work_sheet.write(0, h, head[h])

    # 添加构造的随机数据
    for i in range(n):
        name = fake.name_male()
        phone = fake.phone_number()
        id_card = fake.ssn()
        birthday = fake.date()
        xb = fake.last_name_female()
        address = fake.address()
        work_sheet.write(i + 1, 0, name)
        work_sheet.write(i + 1, 1, xb)
        work_sheet.write(i + 1, 2, id_card)
        word_sheet.write(i + 1, 3, birthday)
        word_sheet.write(i + 1, 4, phone)
        word_sheet.write(i + 1, 5, address)

    work_book.save(save_path)


def save_to_excel2(save_path, n):
    res = []
    # 生成 n 条数据
    for i in range(n):
        res.append([fake.name_male(), fake.last_name_female(),
                    fake.ssn(), fake.date(), fake.phone_number(), fake.address()])

    # list转dataFrame
    df = pd.DataFrame(data=res, columns=[
                      '姓名', '性别', '身份证号', '出生日期', '手机号', '家庭地址'])

    # 保存到本地excel
    df.to_excel(save_path, index=False)


if __name__ == '__main__':
    save_name = '测试数据11'
    save_path = 'D:\\jupyter notebook\\数据\\' + save_name + '.xls'
    n = 20
    # save_to_excel(save_name, save_path, n)
    save_to_excel2(save_path, n)


# 第二示例


fake = Faker('zh_CN')


def save_to_excel(save_name, save_path, n):
    work_book = xlwt.Workbook(encoding='utf-8')
    work_sheet = work_book.add_sheet(save_name)

    # 添加字段名
    head = ['姓名', '身份证号', '出生日期', '手机号', '家庭地址']
    for h in range(len(head)):
        work_sheet.write(0, h, head[h])

    # 添加构造的随机数据
    for i in range(n):
        name = fake.name_male()
        phone = fake.phone_number()
        id_card = fake.ssn()
        birthday = fake.date_between(start_date=1977-1-1, end_date=2015-1-1)
        address = fake.address()
        work_sheet.write(i + 1, 0, name)
        work_sheet.write(i + 1, 1, id_card)
        word_sheet.write(i + 1, 2, birthday)
        word_sheet.write(i + 1, 3, phone)
        word_sheet.write(i + 1, 4, address)

    work_book.save(save_path)


def save_to_excel2(save_path, n):
    res = []
    # 生成 n 条数据
    for i in range(n):
        res.append([fake.name_male(), fake.ssn(), fake.date_between(),
                    fake.phone_number(), fake.address()])

    # list转dataFrame
    df = pd.DataFrame(data=res, columns=['姓名', '身份证号', '出生日期', '手机号', '家庭地址'])

    # 保存到本地excel
    df.to_excel(save_path, index=False)


if __name__ == '__main__':
    save_name = '测试数据end'
    save_path = 'D:\\jupyter notebook\\数据\\' + save_name + '.xls'
    n = 150
    # save_to_excel(save_name, save_path, n)
    save_to_excel2(save_path, n)
