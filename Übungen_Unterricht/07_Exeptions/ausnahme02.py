class A():
    print('Initiator, probably')  # Initiator

    def __new__(cls):
        return super().__new__(cls)

    infotext = 'Das ist ein Infotext!'
    
    print('Ja ober Klasse!')  # Initiator

    def sag_hallo(self, name='Dagobert'):
        self.name = name
        print('Hallo')

    def gib_name_aus(self):
        print(self.name)


class B(A):
    def sag_tschuess(self):
        print('Schüss')


b = B()
a = A()
B()
B()
A()
exit(1)

b.sag_hallo()
b.sag_tschuess()

a.sag_hallo()
b.name = 'Donald'

b.gib_name_aus()
a.gib_name_aus()

print(A.infotext)
A.infotext = 'Wech...'
print(B.infotext)
