class Empty:

    def __init__(self):
        # nothing to do!
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())


class Node:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return False

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self

def inorder(root, lst = []):
    
    return [self.left.inorder() + root + self.right.inorder()]

def min_item(root):
    if root.is_empty():
        return None
    items = inorder(root, lst = [])
    return items[0]
       
def max_item(root):
    if root.is_empty():
        return None
    items = inorder(root, lst = [])
    return items[-1]

def balance_factor(root):
    if root.is_empty():
        return None
    return root.right.height() - root.left.height()

def balanced_everywhere(root):
    if not -1 <= root.balance_factor <= 1:
        return False
    else:
        if not (root.is_empty() or root.is_leaf()):
            balanced_everywhere(root.left)
            balanced_everywhere(root.right)
    
    return True

def add_to_all(root, integer):
    if not root.is_empty():
        root.value = root.value + integer
        if not root.is_leaf():
            add_to_all(root.left, integer)
            add_to_all(root.right, integer)

def path_to(root, integer):


def __str__(root)
            


if __name__ == "__main__":
    bst = Empty().insert(42).insert(10).insert(15).insert(63)

    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")
