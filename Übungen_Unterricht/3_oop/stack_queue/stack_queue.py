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

    def pop(self):
        """Entfernt das erste Element aus der Queue (ähnlich wie dequeue) und gibt es zurück."""
        return self.dequeue()

    def is_empty(self):
        """Überprüft, ob die Queue leer ist."""
        return len(self.queue) == 0

    def peek(self):
        """Gibt das erste Element der Queue zurück, ohne es zu entfernen."""
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue ist leer"
