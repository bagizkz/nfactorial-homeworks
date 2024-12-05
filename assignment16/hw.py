from typing import List, Any, Dict, Set, Generator




class StaticArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None] * capacity

    def set(self, index: int, value: int) -> None:
        if index < 0 or index >= self.capacity:
            raise IndexError("index за пределои")
        self.data[index] = value

    def get(self, index: int) -> int:
        if index < 0 or index >= self.capacity:
            raise IndexError("index за пределом")
        return self.data[index]



class DynamicArray:
    def __init__(self):
        self.data = []
        self.size = 0

    def append(self, value: int) -> None:
        self.data.append(value)
        self.size += 1

    def insert(self, index: int, value: int) -> None:
        if index < 0 or index > self.size:
            raise IndexError("index за пределом")
        self.data.insert(index, value)
        self.size += 1

    def delete(self, index: int) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("index за пределом")
        self.data.pop(index)
        self.size -= 1

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            raise IndexError("index за пределом")
        return self.data[index]




class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1


    def insert(self, position: int, value: int) -> None:
        if position < 0 or position > self._size:
            raise IndexError("за пределами поля")
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None: 
                self.tail = new_node
        self._size += 1


    def delete(self, value: int) -> None:
        current = self.head
        prev = None
        while current is not None:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                    if self.head is None:
                        self.tail = None
                else:
                    prev.next = current.next
                    if current.next is None:
                        self.tail = prev
                self._size -= 1
                return
            prev = current
            current = current.next
        raise ValueError("не найден")

    def find(self, value: int) -> Node:
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        raise ValueError("не найден")

    def size(self) -> int:
        return self._size


    def is_empty(self) -> bool:
        return self._size == 0


    def print_list(self) -> None:
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    
    def reverse(self) -> None:
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head, self.tail = self.tail, self.head
    
    def get_head(self) -> Node:
        return self.head

    
    def get_tail(self) -> Node:
        return self.tail


class DoubleNode:
    def __init__(self, value: int, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value: int) -> None:
        new_node = DoubleNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    def insert(self, position: int, value: int) -> None:
        if position < 0 or position > self._size:
            raise IndexError("за предлом")
        new_node = DoubleNode(value)
        if position == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
            if new_node.next is None:
                self.tail = new_node
        self._size += 1

    def delete(self, value: int) -> None:
        current = self.head
        while current is not None:
            if current.value == value:
                if current.prev is None:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                    if current.next is None:
                        self.tail = None
                else:
                    current.prev.next = current.next
                    if current.next is not None:
                        current.next.prev = current.prev
                    if current.next is None:
                        self.tail = current.prev
                self._size -= 1
                return
            current = current.next
        raise ValueError("не найден")

    def find(self, value: int) -> DoubleNode:
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        raise ValueError("не найден")

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def print_list(self) -> None:
        current = self.head
        while current is not None:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def reverse(self) -> None:
        current = self.head
        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def get_head(self) -> DoubleNode:
        return self.head

    def get_tail(self) -> DoubleNode:
        return self.tail








class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value: int) -> None:
        self.items.append(value)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("пусто")
        return self.items.pop(0)

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("пусто")
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0





class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None



class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node: TreeNode, value: int) -> None:
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)


    def delete(self, value: int) -> None:
        self.root = self._delete(self.root, value)

    def _delete(self, node: TreeNode, value: int) -> TreeNode:
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_larger_node = self._get_min(node.right)
                node.value = min_larger_node.value
                node.right = self._delete(node.right, min_larger_node.value)

        return node



    def search(self, value: int) -> TreeNode:
        return self._search(self.root, value)

    def _search(self, node: TreeNode, value: int) -> TreeNode:
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)



    def inorder_traversal(self) -> List[int]:
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node: TreeNode) -> List[int]:
        if node is None:
            return []
        return self._inorder_traversal(node.left) + [node.value] + self._inorder_traversal(node.right)


    def size(self) -> int:
        return self._size(self.root)

    def _size(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)



    def is_empty(self) -> bool:
        return self.root is None

    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))


    def preorder_traversal(self) -> List[int]:
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, node: TreeNode) -> List[int]:
        if node is None:
            return []
        return [node.value] + self._preorder_traversal(node.left) + self._preorder_traversal(node.right)



    def postorder_traversal(self) -> List[int]:
        return self._postorder_traversal(self.root)

    def _postorder_traversal(self, node: TreeNode) -> List[int]:
        if node is None:
            return []
        return self._postorder_traversal(node.left) + self._postorder_traversal(node.right) + [node.value]


    def level_order_traversal(self) -> List[int]:
        if self.root is None:
            return []

        queue = [self.root]
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result


    def minimum(self) -> TreeNode:
        current = self.root
        while current and current.left:
            current = current.left
        return current

    def maximum(self) -> TreeNode:
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    
    def is_valid_bst(self) -> bool:
        return self._is_valid_bst(self.root, float('-inf'), float('inf'))

    def _is_valid_bst(self, node: TreeNode, min_val: int, max_val: int) -> bool:
        if node is None:
            return True
        if not (min_val < node.value < max_val):
            return False
        return self._is_valid_bst(node.left, min_val, node.value) and self._is_valid_bst(node.right, node.value, max_val)
    

# Сортировки

def insertion_sort(lst: List[int]) -> List[int]:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def selection_sort(lst: List[int]) -> List[int]:
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def shell_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst


def merge_sort(lst: List[int]) -> List[int]:
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

    return lst


def quick_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
