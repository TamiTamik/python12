x = 99
try:
    x = x + 1
except NameError as error:
    x = -1
finally:
    print('finish', x)
