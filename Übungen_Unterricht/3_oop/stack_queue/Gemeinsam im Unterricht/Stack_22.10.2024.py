
# Ein Stack ist wie ein Queue, eine Liste oder (An-)Sammlung

from typing import override


class Stack(list):  
     
    def push(self, item) -> None:
        super().append(item)

    @override
    def pop(self) -> object:
        if len(self) == 0:
            print('Nichts da zum entfernen.')
            return None

        return super().pop()


class Limited_Stack(Stack):
    @override

    def __init__(self, limit):
        super()
        self.limit = limit
    @override
    def push(self, item) -> bool:
        if len(self) == self.limit:
            print('Dubbele, isch voll!')
            return False
        self.append(item)
        return True


def run2():
    l = Limited_Stack(3)
    l.push('1')
    l.push('2')
    l.push('3')
    print(l)
    if not l.push('4'):
        print('Wirklich voll!')
    print(l)


def run():
    stack01 = Stack()
    stack01.push('Regenschirm')
    print(stack01)
    stack01.push('Regentonne')
    stack01.push('Vegane Bratwurst')
    stack01.push('Bratwurst')
    print(stack01)
    stack01.pop()
    print(stack01)
    stack01.pop()
    stack01.pop()
    print(stack01)



if __name__ == '__main__':
    run2()
