class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Fügt ein Element am Ende des Stacks hinzu."""
        self.stack.append(item)

    def pop(self):
        """Entfernt das letzte Element aus dem Stack und gibt es zurück."""
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack ist leer"

    def is_empty(self):
        """Überprüft, ob der Stack leer ist."""
        return len(self.stack) == 0

    def peek(self):
        """Gibt das letzte Element des Stacks zurück, ohne es zu entfernen."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack ist leer"

    def show(self):
        """Zeigt den aktuellen Stack."""
        return self.stack if not self.is_empty() else "Stack ist leer"


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Fügt ein Element am Ende der Queue hinzu."""
        self.queue.append(item)

    def dequeue(self):
        """Entfernt das erste Element aus der Queue und gibt es zurück."""
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue ist leer"

    def is_empty(self):
        """Überprüft, ob die Queue leer ist."""
        return len(self.queue) == 0

    def peek(self):
        """Gibt das erste Element der Queue zurück, ohne es zu entfernen."""
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue ist leer"

    def show(self):
        """Zeigt die aktuelle Queue."""
        return self.queue if not self.is_empty() else "Queue ist leer"


# Beispielhafte Verwendung von Stack und Queue
if __name__ == "__main__":
    # Stack Beispiel
    my_stack = Stack()
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    print("Initialer Stack:", my_stack.show())  # Zeigt den gesamten Stack

    print("Stack pop:", my_stack.pop())  # Entfernt das letzte Element (30)
    print("Stack nach pop:", my_stack.show())  # Zeigt den neuen Stack

    # Queue Beispiel
    my_queue = Queue()
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)

    print("\nInitiale Queue:", my_queue.show())  # Zeigt die gesamte Queue

    print("Queue dequeue:", my_queue.dequeue())  # Entfernt das erste Element (10)
    print("Queue nach dequeue:", my_queue.show())  # Zeigt die neue Queue
