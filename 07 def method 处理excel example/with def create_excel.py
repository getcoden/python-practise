import os


def create_excel():
    """
    创建excel文件
    :return:
    """
    file_path = os.path.dirname(os.path.abspath('D:/')) + "/demo.xlsx"
    df = pd.DataFrame(columns=["title", "content"])
    df.to_excel(file_path, index=False)


create_excel()
