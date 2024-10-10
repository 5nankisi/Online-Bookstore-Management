from abc import ABC
from node import Node


class LinkedList(ABC):
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head

            while pointer:
                if pointer.next is None:
                    pointer.next = Node(elem)
                    break
                pointer = pointer.next
        else:
            self.head = Node(elem)

        self._size += 1

    def __len__(self):
        return self._size

    def __getitem__(self, item):
        pointer = self.head

        for i in range(item):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")

        if pointer:
            return pointer.data
        raise IndexError("List index out of range")

    def remove(self, elem):
        if self.head is None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next

            self._size -= 1

            return True
        else:
            pointer = self.head
            state = False

            i = 0

            while pointer:
                if pointer.data == elem:
                    state = True
                    break
                pointer = pointer.next
                i += 1

            pointer1 = self.head
            for i in range(i - 1):
                if pointer1:
                    pointer1 = pointer1.next
                else:
                    raise IndexError("List index out of range")

            pointer1.next = pointer.next
            pointer.next = None

            if state is True:
                self._size -= 1
                return True

            return False
