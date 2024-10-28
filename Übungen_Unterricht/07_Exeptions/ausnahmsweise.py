def division(a, b):
    return a / b


print(division(2, 3))
print(division(14, 2))


try:
    print(division(2, 0))
except ZeroDivisionError as e:
    print(e)
    print('Ja ne, is kla..:')
finally:
    print("Daswollt' ich am Schluss noch sagen!")
    