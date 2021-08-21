from pdf2docx import Converter
from configparser import ConfigParser
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from xlrd import *

import fitz
import os
import pandas as pd
import sys
import openpyxl
from win32com.client import constants, gencache


class Main_Win(QWidget):
    def __init__(self):
        self.i = 0
        self.filename = ""
        super(Main_Win, self).__init__()
        self.setAcceptDrops(True)
        self.Main_WinUI()

    def Main_WinUI(self):
        self.setWindowTitle('多功能系统')
        self.resize(1700, 880)

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) // 2
        newTop = (screen.height() - size.height()) // 2
        self.move(newLeft, newTop)
        # self.setFixedSize(1700,880)

        palette = QPalette()

        pix = QPixmap(os.getcwd()+"\\images\\six.png")
        pix = pix.scaled(1300, 880)
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)

        self.setToolTip('温馨提示:软件仅供参考，有问题可以上论坛交流！')
        QToolTip.setFont(QFont('Times', 10, QFont.Black))

        self.setWindowIcon(QIcon(os.getcwd()+'\\images\\Book.ico'))
        print(os.getcwd()+'\\images\\Book.ico')

        self.Main_WinLayout()
        self.show()

    def Main_WinLayout(self):

        self.group = QGroupBox(self)
        self.group.setTitle('参数设置区')
        self.group.setGeometry(10, 10, 400, 300)
        self.layout = QGridLayout()

        self.label_one = QLabel('<font color=#9370DB>请输入要搜索的关键词：<\\font>')
        self.layout.addWidget(self.label_one, 0, 0)

        self.edit_one = QLineEdit()
        self.edit_one.setAlignment(Qt.AlignCenter)
        self.edit_one.setPlaceholderText('这里输入要搜索的关键词')
        self.layout.addWidget(self.edit_one, 0, 1)

        self.button_one = QPushButton('开始搜索')
        self.layout.addWidget(self.button_one, 1, 0)
        self.button_one.clicked.connect(self.dialoginfo)
        self.button_two = QPushButton('导入文件')
        self.layout.addWidget(self.button_two, 1, 1)
        self.button_two.clicked.connect(self.groove_five)

        self.button_four = QPushButton('PDF转图片')
        self.layout.addWidget(self.button_four, 2, 0)
        self.button_four.clicked.connect(self.Start_PDF_Image)
        self.button_five = QPushButton('Word转PDF')
        self.layout.addWidget(self.button_five, 2, 1)
        self.button_five.clicked.connect(self.Start_Word_PDF)

        self.button_six = QPushButton('PDF转Word')
        self.layout.addWidget(self.button_six, 3, 0)
        self.button_six.clicked.connect(self.Start_PDF_Word)

# ---------------------------------------------------------------

        self.group_two = QGroupBox(self)
        self.group_two.setTitle('输出日志')
        self.group_two.setGeometry(10, 320, 400, 550)
        self.textedit_one = QTextEdit()
        self.textedit_one.setHtml('<font color=red>温馨提示！<\\font>')
        self.textedit_one.setFont(QFont("Times", 10))
        self.textedit_one.moveCursor(QTextCursor.End)
        self.textedit_one.insertPlainText("\n目前软件只支持Excel,Word，PDF文件\n")

        self.layout_two = QGridLayout()
        self.textedit_one.setReadOnly(True)
        self.layout_two.addWidget(self.textedit_one)
        self.group_two.setLayout(self.layout_two)

        self.group_three = QGroupBox(self)
        self.layout_two = QHBoxLayout()
        self.group_three.setTitle('订单数据')
        self.group_three.setGeometry(420, 10, 1265, 860)
        self.table_one = QTableWidget()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showMenu)
        self.contextMenu = QMenu(self)
        self.CP = self.contextMenu.addAction('复制')
        self.CP.triggered.connect(
            lambda: self.selected_tb_text(self.table_one))
        self.CP = self.contextMenu.addAction('打开表格可编辑')
        self.CP.triggered.connect(lambda: self.compile_True(self.table_one))
        self.CP = self.contextMenu.addAction('关闭表格可编辑')
        self.CP.triggered.connect(lambda: self.compile_False(self.table_one))
        self.CP = self.contextMenu.addAction('添加数据')
        self.CP.triggered.connect(lambda: self.appendinfo(self.table_one))

        self.layout_two.addWidget(self.table_one)
        self.group_three.setLayout(self.layout_two)
        QApplication.processEvents()

        self.group.setLayout(self.layout)

    def dialoginfo(self):
        find_str = []
        if self.filename:
            if self.edit_one.text() == "":
                reply = QMessageBox.question(
                    win, '温馨提示！', '大哥，你关键字，怎么也输点吧！', QMessageBox.Yes | QMessageBox.No, (QMessageBox.Yes))
                if reply == QMessageBox.Yes:
                    pass
                else:
                    self.dialoginfo()
            else:
                for i in self.data.to_dict('records'):
                    for value in i.values():
                        if str(value) == str(self.edit_one.text()):
                            find_str.append(i)
                print(find_str)
                if len(find_str):
                    self.textedit_one.moveCursor(QTextCursor.End)
                    self.textedit_one.insertPlainText(
                        f"\n查询成功！！一共{len(find_str)}条数据！！\n")
                    self.table_one.setRowCount(len(find_str))
                    self.table_one.clearContents()
                    for s in range(len(find_str)):
                        for key, value in find_str[s].items():
                            item = QTableWidgetItem(str(value))
                            item.setTextAlignment(Qt.AlignCenter)
                            self.table_one.setItem(
                                s, self.head_list.index(key), item)
                else:
                    self.textedit_one.moveCursor(QTextCursor.End)
                    self.textedit_one.insertPlainText(f"\n查询失败，找不到该条信息！！！\n")
        else:
            reply = QMessageBox.question(
                win, '温馨提示！', '请先导入文件在查询！！', QMessageBox.Yes | QMessageBox.No, (QMessageBox.Yes))
            if reply == QMessageBox.Yes:
                pass
            else:
                self.dialoginfo()

    def selected_tb_text(self, table_view):
        try:
            indexes = table_view.selectedIndexes()
            indexes_dict = {}
            for index in indexes:
                row, column = index.row(), index.column()
                if row in indexes_dict.keys():
                    indexes_dict[row].append(column)
                else:
                    indexes_dict[row] = [column]
            print(indexes_dict)
            print(row, column)
            text = []
            for row, columns in indexes_dict.items():
                row_data = []
                for column in columns:
                    try:
                        data = table_view.item(row, column).text()
                    except BaseException as e:
                        data = ' '
                    finally:
                        if row_data:
                            row_data = ' ' + data
                        else:
                            row_data = data

                        if text:
                            if len(text) % 4 == 0:
                                text.append('\n')
                            text.append(row_data)
                        else:
                            text.append(row_data)
            print(text)
            text_two = ''
            for item in text:
                text_two += item
            try:
                clipboard = QApplication.clipboard()
                clipboard.setText(text_two)  # 复制到粘贴板
            except BaseException as e:
                print(e)
        except BaseException as e:
            print(e)
            clipboard = QApplication.clipboard()
            clipboard.setText(text_two)
            return ''

    def keyPressEvent(self, event):     # 重写键盘监听事件
        # 监听 CTRL+C 组合键，实现复制数据到粘贴板
        if (event.key() == Qt.Key_C) and QApplication.keyboardModifiers() == Qt.ControlModifier:
            text = self.selected_tb_text(self.table_one)

    def showMenu(self, pos):
        print(pos)
        self.contextMenu.exec_(QCursor.pos())

    def groove_five(self):
        self.textedit_one.moveCursor(QTextCursor.End)
        self.textedit_one.insertPlainText("\n正在导入Excel文件..............\n")
        self.filename, ok = QFileDialog.getOpenFileName(
            self, '想好了在选，记得选EXCAL文件！！！！', 'C:\\', '文件类型默认所有，这个你不用担心：(*.*)')
        self.excal()

    def excal(self):
        print(self.filename)
        self.head_list = []
        self.sum_list = []
        if self.filename[-4:] == "xlsx" or self.filename[-3:] == "xls":
            self.textedit_one.moveCursor(QTextCursor.End)
            self.textedit_one.insertPlainText("\n导入成功！\n")
            self.textedit_one.moveCursor(QTextCursor.End)
            self.textedit_one.insertPlainText(
                f'\n成功导入Excel文件!,路径为：{self.filename}\n')
            self.data = pd.read_excel(self.filename)
            print("123")
            for i in self.data:
                self.head_list.append(i)
            self.table_one.setRowCount(len(self.data[i].values))
            self.table_one.setColumnCount(len(self.head_list))
            self.table_one.setHorizontalHeaderLabels(self.head_list)

            for j in self.head_list:
                for k in self.data[j].values:
                    s = QTableWidgetItem(str(k))
                    s.setTextAlignment(Qt.AlignCenter)
                    self.sum_list.append(k)
                    self.table_one.setItem(
                        len(self.sum_list) - 1, int(self.head_list.index(j)), s)
                self.sum_list.clear()
            self.textedit_one.moveCursor(QTextCursor.End)
            self.textedit_one.insertPlainText(
                f'目前有{len(self.data[j].values)}条数据！\n')
            self.table_one.setEditTriggers(
                QAbstractItemView.NoEditTriggers)  # 设置单元格不可编辑

        elif self.filename[-4:] == "docx":
            self.textedit_one.moveCursor(QTextCursor.End)
            self.textedit_one.insertPlainText("\n导入成功！\n")
            self.textedit_one.moveCursor(QTextCursor.End)
            self.textedit_one.insertPlainText(
                f'\n成功导入Word文件!,路径为：{self.filename}\n')
        elif self.filename[-3:] == "pdf":
            self.textedit_one.moveCursor(QTextCursor.End)
            self.textedit_one.insertPlainText("\n导入成功！\n")
            self.textedit_one.moveCursor(QTextCursor.End)
            self.textedit_one.insertPlainText(
                f'\n成功导入PDF文件!,路径为：{self.filename}\n')
        elif os.path.isdir(self.filename):
            self.textedit_one.moveCursor(QTextCursor.End)
            self.textedit_one.insertPlainText("\n导入成功！\n")
            self.textedit_one.moveCursor(QTextCursor.End)
            self.textedit_one.insertPlainText(
                f'\n成功导入内含PDF文件的文件夹!,路径为：{self.filename}\n')

        else:
            self.textedit_one.moveCursor(QTextCursor.End)
            self.textedit_one.insertPlainText(
                "\n导入失败，请检查是否导入的是后缀为：xlsx,docx，pdf的文件！\n")

    def Queryinfomation(self):
        for i in range(self.shape[0]):
            for i2 in range(self.shape[1]):
                Query = self.table_one.item(i, i2).text()
                print(Query)

    def compile_True(self, table_view):
        self.table_one.setEditTriggers(QAbstractItemView.DoubleClicked)

    def compile_False(self, table_view):
        self.table_one.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def appendinfo(self, table_view):
        self.i += 1
        self.table_one.setRowCount(self.i)

    def dragEnterEvent(self, QDragEnterEvent):
        if QDragEnterEvent.mimeData().hasText():
            QDragEnterEvent.acceptProposedAction()

    def dropEvent(self, QDropEvent):
        self.filename = QDropEvent.mimeData().text().replace('file:///', '')
        print(self.filename)
        self.excal()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Message', '确定要退出吗?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()
        else:
            event.ignore()

    def pyMuPDF_fitz(self, pdfPath, imagePath):
        pdfDoc = fitz.open(pdfPath)
        for pg in range(pdfDoc.pageCount):
            page = pdfDoc[pg]
            rotate = int(0)
            zoom_x = 1.33333333
            zoom_y = 1.33333333
            mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pix = page.getPixmap(matrix=mat, alpha=False)

            if not os.path.exists(imagePath):
                os.makedirs(imagePath)
            pix.writePNG(imagePath + '/' + 'images_%s.png' % pg)

    def Start_Word_PDF(self):
        if self.filename[-4:] == "docx" or self.filename[-3:] == "dox":
            reply = QMessageBox.question(
                win, '温馨提示！', '程序开始执行时，因为计算量大可能会导致卡顿，这是正常现象，请不要乱点，请耐心稍等一会儿！！！', QMessageBox.Yes | QMessageBox.No, (QMessageBox.Yes))
            if reply == QMessageBox.Yes:
                pass
            else:
                self.Start_Word_PDF()

            Word_pdf_path = self.filename.replace(self.filename[-4:], "pdf")
            word = gencache.EnsureDispatch('Word.Application')
            doc = word.Documents.Open(self.filename, ReadOnly=1)
            doc.ExportAsFixedFormat(Word_pdf_path, constants.wdExportFormatPDF,
                                    Item=constants.wdExportDocumentWithMarkup, CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
            word.Quit(constants.wdDoNotSaveChanges)
            self.textedit_one.moveCursor(QTextCursor.End)
            self.textedit_one.insertPlainText(
                f"\nWord文件已成功转换PDF文件，请前往Word同目录下查看！！！\n\n生成路径为:{Word_pdf_path}\n")
        else:
            QMessageBox.question(win, '温馨提示！', '请检查是否为Word文件！！',
                                 QMessageBox.Yes | QMessageBox.No, (QMessageBox.Yes))

    def Start_PDF_Image(self):
        if self.filename[-3:] == "pdf":
            reply = QMessageBox.question(
                win, '温馨提示！', '程序开始执行时，因为计算量大可能会导致卡顿，这是正常现象，请不要乱点，耐心稍等一会儿！！！', QMessageBox.Yes | QMessageBox.No, (QMessageBox.Yes))
            if reply == QMessageBox.Yes:
                pass
            else:
                self.Start_PDF_Image()

            self.textedit_one.moveCursor(QTextCursor.End)
            self.textedit_one.insertPlainText(f'\n正在转换PDF图片，\n')
            PDF_images_path = os.path.join(
                os.path.expanduser("~"), 'Desktop//PDF_images')
            self.pyMuPDF_fitz(self.filename, PDF_images_path)
            self.textedit_one.moveCursor(QTextCursor.End)
            self.textedit_one.insertPlainText(
                f'\nPDF文件已成功转换图片文件，请前往桌面查看！！！\n\n生成路径为:{PDF_images_path}\n')

        else:
            QMessageBox.question(win, '温馨提示！', '请检查是否为PDF文件！！',
                                 QMessageBox.Yes | QMessageBox.No, (QMessageBox.Yes))

    def Start_PDF_Word(self):
        if os.path.isdir(self.filename):
            QMessageBox.question(win, '温馨提示！', '程序开始执行时，因为计算量大可能会导致卡顿，这是正常现象，请不要乱点，耐心稍等一会儿！！！',
                                 QMessageBox.Yes | QMessageBox.No, (QMessageBox.Yes))
            config_parser = ConfigParser()
            config_parser.read('config.cfg', encoding='utf-8')
            config = config_parser['default']
            for file in os.listdir(self.filename):
                extension_name = os.path.splitext(file)[1]
                if extension_name != '.pdf':
                    continue
                file_name = os.path.splitext(file)[0]
                pdf_file = self.filename + '/' + file
                word_file = self.filename + '/' + file_name + '.docx'

                cv = Converter(pdf_file)
                cv.convert(word_file)
                cv.close()
                self.textedit_one.moveCursor(QTextCursor.End)
                self.textedit_one.insertPlainText(
                    f'\nPDF文件已成功转换图片文件，请前往桌面查看！！！\n\n生成路径为:{word_file}\n')
        else:
            QMessageBox.question(win, '温馨提示！', '请导入一个内含PDF文件的文件夹！！！',
                                 QMessageBox.Yes | QMessageBox.No, (QMessageBox.Yes))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Main_Win()
    sys.exit(app.exec_())
