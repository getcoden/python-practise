import re


def get_phone_number(str):
    res = re.findall(
        r'(^(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$)', str)
    return res


print(get_phone_number('23:12:12'))
