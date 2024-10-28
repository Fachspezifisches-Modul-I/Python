from stack_queue import Stack, Queue

# Stack
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
print("Stack peek:", my_stack.peek()) # Gibt 10 zurück
print("Stack pop:", my_stack.pop())  # Gibt 20 zurück
print("Stack peek:", my_stack.peek()) # Gibt 10 zurück

# Queue
my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
print("Queue peek:", my_queue.peek()) # Gibt 20 zurück
print("Queue pop:", my_queue.pop())   # Gibt 10 zurück (ähnlich wie dequeue)
print("Queue peek:", my_queue.peek()) # Gibt 20 zurück