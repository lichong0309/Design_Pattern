from collections.abc import Iterable, Iterator
from typing import Any, List

"""
在python中，可以直接使用collections.abc模块构造迭代器
Iterable中的__iter__()方法和Iterator中的__next__ ()
"""

class AlphabeticalOrderIterator(Iterator):
    """
    具体迭代器，执行遍历算法，需要存储迭代位置索引。
    """
    _position = None #存储迭代位置索引
    _reverse = False #迭代方向，默认为正向

    def __init__(self, collection, reverse=False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        返回序列的下一个值，如果已经到序列的最后一个值，返回StopIteration异常
        :return: 序列的下一个值
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value

class WordsCollection(Iterable):
    """
    聚合迭代器，根据输入的collection对象，返回合适的可迭代对象
    """
    def __init__(self, collection: List[Any] = []):
        self._collection = collection

    def __iter__(self):
        """
        :return: 返回迭代对象本身
        """
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self):
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)

def main():
    """
    client端不需要知道迭代器的具体细节，只需要知道聚合迭代器规定的入口。聚合函数根据输入自动寻找合适的迭代器对象
    """
    collection = WordsCollection()
    collection.add_item("One")
    collection.add_item("Python")
    collection.add_item("Hello")
    print("正向：")
    print(', '.join(collection))
    print("反向：")
    print(", ".join(collection.get_reverse_iterator()))

if __name__ == "__main__":
    main()
