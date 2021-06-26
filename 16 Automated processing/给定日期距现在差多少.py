# 计算女朋友的生日离现在还有几天
def get_days(birthday: str) -> int:
    splits = re.split(r'[-.\s+/]', birthday)
    splits = [s for s in splits if s]
    if len(splits) < 3:
        raise ValueError('输入格式不正确， 至少包括年月日')

    splits = splits[:3]  # 只截取年月日
    birthday = datetime.strptime('-'.join(splits), '%Y-%m-%d')
    tod = date.today()
    delta = birthday.date() - tod
    return delta.days


print(get_days('2021-09-24'))     # 98
