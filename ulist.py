from .errors import LinkedListUnderflow


class UList(object):
    """docstring for UList"""
    def __init__(self):
        super(UList, self).__init__()
        self._head = None

    def is_empty(self):
        return self._head is None

    def len(self):
        p, n = self._head, 0
        while p is not None:
            n += 1
            p = p.next
        return n

    def pre_append(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self.is_empty():
            self._head = LNode(elem, None) 
            return

        p = self._head
        # O(n), 取决于长度，后期记录plast
        while p.next is not None:
            p = p.next

        p.next = LNode(elem, None)
        return

    def pop_last(self):
        if self.is_empty():
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e

        while p.next.next is not None:
            p = p.next
            pass

        e = p.next.elem
        p.next = None
        return e

    def find(self, func):
        """
        find  查找满足一定条件的元素
        :param func:  满足某个过滤条件的方法，接收elem
        :return: 过滤到的结果
        """
        p = self._head
        while p is not None:
            if func(p.elem):
                return p.elem
            p = p.next

    def print_all(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
