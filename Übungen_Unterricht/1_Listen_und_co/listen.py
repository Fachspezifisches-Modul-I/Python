# Listen funktionieren wie die ArrayList in Java

liste = ('Äpfel', 'Birnen', 'Tomaten')
print (liste, end=' ')
print ('\n')
print (liste[1],) #Birnen
print ('\n')
print ('For-Each-Konstrukt')

# for-each
for i in liste:
    print(i)
print()

liste = [12, 45, 89, 4]
print ('\n')
print ('Liste mit Zahlenwerten')
for i in liste:
    print (i, end='-')
print(sum(liste))