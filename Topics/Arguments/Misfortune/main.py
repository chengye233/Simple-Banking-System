f = 3.14  # the type is float
print(type(f))  # <class 'float'>

s = str(f)  # converting float to string
print(type(s))  # <class 'str'>

i = int(f)  # while converting a float value to an integer its fractional part is discarded
print(i)  # 3
print(type(i))  # <class 'int'>

f = float(i)
print(f)  # 3.0
print(type(f))  # <class 'float'>