def rs(data):
    if len(data) > 1:
        return data[0] + rs(data[1:])
    else:
        return data[0]


# print(rs([4, 5, 7, 9, 10]))

# strip.py

data = [
    'alpha\n',
    'beat\n',
    'gamma\n'
]

print(data)

# data = [s.strip() for s in data]
# print(data)

'''
def strip(s):
    return s.strip()


data = list(map(strip, data))
print(data)
'''
data = list(map(lambda s: s.strip(), data))
print(data)
