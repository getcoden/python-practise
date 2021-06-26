#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pyperclip
'this is an regex program for American phone and email'

# TODO: Create American phone regex.
import re
phoneRegex = re.compile(r'''(
    (\+?86)?    # national code
    (\s|\-)?
    (\d{3,4})   # area code
    (\s|\-)?
    (\d{7,8})   # phone number
    )''', re.VERBOSE)

# TODO: Create email regex.
emailRegex = re.compile(r'''(
    ([\w\%\_\-\+]+)         # emailname
    @                       # emailmark@
    ([\w\.\-]+)             # email domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)

# TODO: Find matches in clipboard text.

text = pyperclip.paste()
d_phone = []
d_email = []
for s in phoneRegex.findall(text):
    phone_num = '-'.join([s[3], s[5]])
    d_phone.append(phone_num)
for s in emailRegex.findall(text):
    d_email.append(s[0])

# TODO: Copy results to the clipboard.
phone_num_str = '\n'.join(d_phone)
email_name_str = '\n'.join(d_email)
matches = phone_num_str + '\n' + email_name_str
pyperclip.copy(matches)
print(matches)

# test = emailRegex.search('my phone num is +86-010-29898928, email is Wu_h@sina.143.com')
