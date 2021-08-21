import smtplib                        # smtplib发送邮件
from email.mime.text import MIMEText  # 构造文本内容
from email.header import Header       # 构造标题内容

'''
# 设置服务器地址
mail_host = "smtp.qq.com"
# 设置服务器端口
mail_port = 465

# 初始化发送方账号
sender = "28480*****@qq.com"
# 初始化接收方账号
receivers = "9152*****@qq.com"

# QQ邮件登录账号
mail_user = "28480*****"
# QQ邮箱第三方授权码
mail_pass = "gwgcqikk********"


def post_email(title, context):
    # 构造文本对象，三个参数：文本内容，设置文本格式,设置编码
    message = MIMEText(context, "plain", "utf-8")
    # 文本对象 添加 发送者
    message["From"] = sender
    # 文本对象 添加 接收者
    message["To"] = receivers
    # 文本对象 添加 标题
    message["Subject"] = Header(title)

    # 创建 SMTP 对象，连接目标服务器
    smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
    # 自己账号登录
    smtpObj.login(mail_user, mail_pass)
    # 发送邮件到目标地址  注意：信息由MTMEText对象 转为 字符串对象
    smtpObj.sendmail(sender, receivers, message.as_string())
    # 结束 SMTP 对象
    smtpObj.quit()


if __name__ == '__main__':
    post_email("至老妖怪的邮件", "老Amy，哪里逃！")


'''

# 打 BOSS 第二版
# 以上实现了发单条邮件的功能，那现在我们就需要实现同时发多条的功能了。嘻嘻～

# 既然接收方的数据信息以行为单位存储在 邮件.xlsx 里面，所以我们需要用 Python 的库 来读取表格数据，
# 为了方便我们仍然使用 pandas.read_excel() 来进行操作。该函数读取的数据返回为 DataFrame 的类型，
# 并且我们还需要将 DataFrame 数据中的每一行为单位，传入到发送邮件的函数中去进行处理发送，
# 所以接下来会使用到 DataFrame.apply(func) 去进行映射。

import smtplib                        # smtplib发送邮件
from email.mime.text import MIMEText  # 构造文本内容
from email.header import Header       # 构造标题内容


# 设置服务器地址
mail_host = "smtp.qq.com"
# 设置服务器端口
mail_port = 465

# 初始化发送方账号
sender = "28480*****@qq.com"

# QQ邮件登录账号
mail_user = "28480*****"
# QQ邮箱第三方授权码
mail_pass = "gwgcqikk********"


def post_email(per_info):
    # 构造文本对象，三个参数：文本内容，设置文本格式,设置编码
    message = MIMEText(per_info["正文"], "plain", "utf-8")
    # 文本对象 添加 发送者
    message["From"] = sender
    # 文本对象 添加 接收者
    message["To"] = per_info["收件人邮箱"]
    # 文本对象 添加 标题
    message["Subject"] = Header(per_info["邮件主题"])

    # 创建 SMTP 对象，连接目标服务器
    smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
    # 自己账号登录
    smtpObj.login(mail_user, mail_pass)
    # 发送邮件到目标地址  注意：信息由MTMEText对象 转为 字符串对象
    smtpObj.sendmail(sender, per_info["收件人邮箱"], message.as_string())
    # 结束 SMTP 对象
    smtpObj.quit()


if __name__ == '__main__':
    # 读取 邮件.xlsx
    email_info_df = pd.read_excel("邮件.xlsx")

    # 使用apply方法 将email_info_df中每一行 映射到post_email函数中
    email_info_df.apply(post_email, axis=1)
