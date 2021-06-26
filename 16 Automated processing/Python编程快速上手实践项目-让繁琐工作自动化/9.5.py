
'''
将一个文件夹备份到一个 ZIP 文件
项目要求：假定你正在做一个项目，它的文件保存在 C:\AlsPythonBook 文件夹中。
你担心工作会丢失， 所以希望为整个文件夹创建一个 ZIP 文件， 作为 “快照” 。
你希望保存不同的版本， 希望 ZIP 文件的文件名每次创建时都有所变化。

'''
#! python3
# backup a folder to zip

import zipfile
import os


def backuptozip(folder):
    folder = os.path.abspath(folder)
    os.chdir(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for root, dirs, files in os.walk(folder):
        print('Adding files in %s...' % root)
        backupZip.write(root.replace(folder, '.\\'))

        for file in files:
            newBase = os.path.basename(folder) + '_'
            if file.startswith(newBase) and file.endswith('.zip'):
                continue
            backupZip.write(os.path.join(root.replace(folder, '.\\'), file))

    backupZip.close()
    print('to_zip Done!')


backuptozip('d:\\test1')
