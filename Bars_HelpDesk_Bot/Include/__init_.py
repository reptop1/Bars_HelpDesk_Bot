a = '5,7'
b = '6,3'
a = a.replace(',','.')
b = b.replace(',','.')

try:
    a = int(a)
    b = int(b)

except Exception as e:
    print("не удалось преобразовать")

try:
    a = float(a)
    b = float(b)

except Exception as e:
    print("не удалось преобразовать 2")

print(a+b)