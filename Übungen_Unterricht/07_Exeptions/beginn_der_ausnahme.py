# Ausnahme

# print(3 / 2)

# print(3 / 0) # Output -> Durch 0 darf man nicht teilen

# Früher
'''zaehler = 3
nenner = 0
if nenner:
    print(zaehler / nenner)
else:
    print('Division durch 0')
'''
# Mit der OOP wurden dann Exceptions und Errors eingeführt
# Compilererror und Laufzeitfehler angucken

try:
    print('Im Try-Block')
    print(3 / 1)
    print('Keiner:r sieht mich :(')

except Exception as e:
    print('Im Except-Block')
    print(e)
finally:
    print('Mich sieht immer jeder!')
