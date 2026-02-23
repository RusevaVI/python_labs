from collections import deque # умеет append, popleft для очередей
from typing import Any, Deque, Optional


class Stack:
    def __init__(self) -> None: #__init__ вызывается при создании объекта: s = Stack()
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
    # Добавить элемент на вершину стека.
        self._data.append(item)

    def pop(self) -> Any:
    # Снять верхний элемент стека и вернуть его.
        if not self._data:
            raise IndexError("Стек пустой")
        return self._data.pop()

    def peek(self) -> Optional[Any]:
    # Вернуть верхний элемент без удаления
        if not self._data:
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)


class Queue:
    def __init__(self) -> None:
        self._data: Deque[Any] = deque() #_data — это deque, и в нём могут быть любые объекты.

    def enqueue(self, item: Any) -> None:
    # Добавить элемент в конец очереди
        self._data.append(item)

    def dequeue(self) -> Any:
    # Взять элемент из начала очереди и вернуть его.
        if not self._data:
            raise IndexError("Очередь пустая")
        return self._data.popleft()

    def peek(self) -> Optional[Any]:
    # Вернуть первый элемент без удаления
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)

if __name__ == "__main__": #— это защита, которая говорит: «этот код только для запуска, не для импорта».
    s = Stack()
    print(s.is_empty())
    s.push(10)
    s.push(20)
    print(s.pop())     # 20
    print(s.peek())    # 10
    print(len(s))      # 1

    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    print(q.dequeue()) # A
    print(q.peek())    # B
    print(len(q))      # 1