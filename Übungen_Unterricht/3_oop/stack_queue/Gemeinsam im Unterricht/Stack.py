class Stack():
    bratwurst = 'Ich bin eine Klassenvariable'

    def __init__(self):
        self.stk = []

    def push(self, item):
        self.stk.append(item)

    def pop(self):
        return self.stk.pop()

    def view(self):
        print(self, stk)


def run():
    st01 = Stack()
    st02 = Stack()

    st01.push('Hallo')
    st02.push('Servas')
    st02.push('Grüß Gott')
    st02.push('Selam aleykum')

    print(st01.stk)
    print(st02.stk)

    st02.pop()
    print(st02.stk)

    print(st01.bratwurst)


if __name__ == '__main__':
    run()
