from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.__len__() == self.capacity:
            if self.current == self.storage.tail:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head
            else:
                self.storage.delete(self.current.next)
                self.current.insert_after(item)
                self.current = self.current.next

        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        if self.storage.head is not None:
            item = self.storage.head
            next_item = item.next
            list_buffer_contents.append(item.value)
            while next_item is not None:
                list_buffer_contents.append(next_item.value)
                item = next_item
                next_item = item.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
