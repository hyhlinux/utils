from ulnode import LNode
from errors import LinkedListUnderflow


class UListBase(object):
    """docstring for UListBase"""

    def __init__(self):
        super(UListBase, self).__init__()
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
            if func and func(p.elem):
                return p.elem
            p = p.next
        return None

    def for_each(self, func):
        p = self._head
        while p is not None:
            func(p.elem)
            p = p.next

    def elements(self, func=None):
        p = self._head
        while p is not None:
            if func and func(p.elem):
                yield p.elem
            p = p.next

    def print_all(self):
        print('\n')
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next


class UList(UListBase):
    """
    优化尾端操作.

    影响: 所有设计变动操作都需要处理
    """
    def __init__(self):
        UListBase.__init__(self)
        self._last = None

    def pre_append(self, elem):
        """
        前端插入:
            1. 空表，插入新元素，self._last指向第一个元素
            2. 非空表，self._last 保持不变
        :param elem:
        :return:
        """
        if self.is_empty():
            self._head = LNode(elem, self._head)
            self._last = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        """
        后端插入:
            1. 空表，插入新元素，self._last/_head指向第一个元素
            2. 非空表，self._head 保持不变, self._last指向最后一个
        :param elem:
        :return:
        """
        if self.is_empty():
            self._head = LNode(elem, None)
            self._last = self._head
        else:
            self._last.next = LNode(elem, None)
            self._last = self._last.next

    def pop_last(self):
        """
        前段删除:
            1. 空表异常
            2. 非空，self._last 弹出，需要找到前一个元素pre, self._last = pre
        :return:
        """
        if self.is_empty():
            raise LinkedListUnderflow('in UList pop')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            self._last = None
            return e

        # 找到倒数第二个元素
        while p.next.next is not None:
            p = p.next

        e = p.next.elem
        p.next = None
        self._last = p
        return e
