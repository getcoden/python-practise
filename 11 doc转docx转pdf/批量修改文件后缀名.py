import os


def batch_rename(work_dir, old_ext, new_ext):
    for filename in os.listdir(work_dir):

        # 获取文件后缀
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        if old_ext == file_ext:   # 定位需要修改后缀名的文件
            newfile = split_file[0] + new_ext   # 修改后文件的完整名称

            # 重命名
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )


batch_rename("D:\pdf", '.csv', '.xlsx')
