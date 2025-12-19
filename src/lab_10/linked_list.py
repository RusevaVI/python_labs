class Node:#Node — это один элемент односвязного спискa
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None #ссылка на первый узел списка, если head is None → список пуст
        self._size = 0 #количество элементов нужно, чтобы len(lst) работал за O(1)

    def append(self, value):
        """Добавить элемент в конец списка"""
        new_node = Node(value)#Создаём новый узел. Пока он не в списке.

        if self.head is None:
            self.head = new_node
            self._size += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        self._size += 1

    def prepend(self, value):
        """Добавить элемент в начало списка"""
        new_node = Node(value, next=self.head)
        self.head = new_node
        self._size += 1

    def insert(self, idx, value):
        """Вставка по индексу"""
        if idx < 0 or idx > self._size:
            raise IndexError("index выходит за предел")

        if idx == 0:
            self.prepend(value) #A-B-D  нужен инд 2 С вст
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next
            if current is None:
                raise IndexError("index за пределом")

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def remove_at(self, idx):
        """Удалить элемент по индексу"""
        if idx < 0 or idx >= self._size:
            raise IndexError("index выходит за предел")

        # если удаляем первый элемент
        if idx == 0:
            self.head = self.head.next
            self._size -= 1
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        # current — узел ПЕРЕД тем, который удаляем
        current.next = current.next.next
        self._size -= 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value #yield — это “верни значение и продолжи потом с этого же места”
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):# когда нужно показать объект как строку.
        return f"SinglyLinkedList({list(self)})"
if __name__ == "__main__":
    lst = SinglyLinkedList()
    lst.append(1)
    lst.append(2)
    lst.prepend(0)
    lst.insert(2, 1.5)

    print(lst)        # SinglyLinkedList([0, 1, 1.5, 2])
    print(len(lst))   # 4

    lst.remove_at(0)
    print(list(lst))  # [1, 2]