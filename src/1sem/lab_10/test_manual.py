from lab_10.structures import Stack, Queue

s = Stack()
s.push(1)
s.push(2)
print(s.pop())   # 2
print(s.peek())  # 1
print(len(s))    # 1

q = Queue()
q.enqueue("a")
q.enqueue("b")
print(q.dequeue())  # a
print(q.peek())     # b
print(len(q))       # 1
from lab_10.linked_list import SinglyLinkedList

lst = SinglyLinkedList()
lst.append(1)
lst.append(2)
lst.prepend(0)
lst.insert(2, 1.5)

print(lst)          # SinglyLinkedList([0, 1, 1.5, 2])
print(len(lst))     # 4

lst.remove(1.5)
lst.remove_at(0)
print(list(lst))    # [1, 2]