# Fakultät in der Mathematik wird mit ! gekennzeichnet

# 5 Fakultät -> 5!
# 5 * 4 * 3 * 2 * 1

# Dazu bitte eine Methode definieren. Die Fakultät soll dabei Variabel sein

def fakultaet(n):
    if n < 0:
        return "Fakultät ist nur für nicht-negative Zahlen definiert"
    elif n == 0 or n == 1:
        return 1
    else:
        ergebnis = 1
        for i in range(2, n + 1):
            ergebnis *= i
        return ergebnis

print(fakultaet(5))   
print(fakultaet(10))  
print(fakultaet(27))  

# 49! / (43! + 6!)