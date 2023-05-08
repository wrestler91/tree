from functools import total_ordering
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None
        self.parent = None
        
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        try:
            hash(value)
        except TypeError:
            raise TypeError('Недопустимое значение для узла')
        else:
            self._data = value

@total_ordering
class Tree:
    def __init__(self, root) -> None:
        if isinstance(root, Node):
            self.root = root
        else:
            self.root = Node(root)
    
    def __find_place(self, new, root) -> object:
        if new.data < root.data:
            if root.left != None:
                return self.__find_place(new, root.left)
        elif new.data > root.data:
            if root.right != None:
                return self.__find_place(new, root.right)
        return root

    def __check_same_data(self, data):
        if type(data) != type(self.root.data):
            raise TypeError('Недопустимое значение для узла')
        if self.find(data):
            raise ValueError('Такой узел уже есть в дереве')
        
        
    def add_node(self, node) -> None:
        if isinstance(node, list):
            for nd in node:
                self.__check_same_data(nd)
                self.add_node(nd)
        else:
            if not isinstance(node, Node):
                self.__check_same_data(node)
                node = Node(node)
            parent = self.__find_place(node, self.root)
            if parent != node:
                node.parent = parent
                if node.data < parent.data:
                    parent.left = node
                elif node.data > parent.data:
                    parent.right = node

    def _del_with_child(self, node, child):
        par = node.parent
        child.parent = par
        node.parent = None
        if par.right == node:
            par.right = child
        else:
            par.left = child
        
    def find_min(self, root):
        if root.left == None:
            return root
        return self.find_min(root.left)
    
    def find(self, data, root = None) -> object:
        if not root:
            root = self.root
        if root.data == data:
            return root
        elif root.data < data and root.right != None:
            return self.find(data, root.right)
        elif root.data > data and root.left != None:
            return self.find(data, root.left)
        
    # доработать так чтобы при передаче числа находил узел дерева для удаления
    def delit(self, data) -> None:
        node = self.find(data)
        if not node:
            raise ValueError('Вершина отсутсвует в дереве')
        par = node.parent
        if node.right == None and node.left == None:
            if par.right == node:
                par.right = None
            elif node.parent.left == node:
                par.left = None
            node.parent = None
            del node
        elif node.right != None and node.left == None:
           self._del_with_child(node, node.right)
        elif node.left != None and node.right == None:
            self._del_with_child(node, node.left)
        else:
            ch = node.right
            if node.right == None:
                ch.parent = node.parent
                node.parent = None
                if par.right == node:
                    par.right = ch
                elif par.left == node:
                    par.left = ch
            else:
                mn = self.find_min(node)
                mn.data = node.data
                self._del_with_child(mn, mn.right)
            del node
    
    
    def show_tree(self, node = False):
        cash = []
        def inner(nd):
            if nd == False:
                nd = self.root
            if nd != None:
                cash.append(nd.data)
                inner(nd.left)
                inner(nd.right)
        inner(node)
        print(*cash)
    
    def __str__(self):
        return f'дерево с корнем {self.root.data}'
    
    # сравнивает по корню
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Tree):
            return self.root.data == __value.root.data
    
    def __lt__(self, __value: object) -> bool:
        if isinstance(__value, Tree):
            return self.root.data < __value.root.data
tree1 = Tree(10)
# tree2 = Tree(5)

# tree1.add_node(5)
# tree1.add_node(15)
tree1.add_node([5, 15, 1, 7, 3, 20])
# tree2.add_node([0, -4, -19, 21, 33, 2])
tree1.delit(7)
tree1.show_tree()
from functools import total_ordering
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None
        self.parent = None
        
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        try:
            hash(value)
        except TypeError:
            raise TypeError('Недопустимое значение для узла')
        else:
            self._data = value

@total_ordering
class Tree:
    def __init__(self, root) -> None:
        if isinstance(root, Node):
            self.root = root
        else:
            self.root = Node(root)
    
    def __find_place(self, new, root) -> object:
        if new.data < root.data:
            if root.left != None:
                return self.__find_place(new, root.left)
        elif new.data > root.data:
            if root.right != None:
                return self.__find_place(new, root.right)
        return root

    def __check_same_data(self, data):
        if type(data) != type(self.root.data):
            raise TypeError('Недопустимое значение для узла')
        if self.find(data):
            raise ValueError('Такой узел уже есть в дереве')
        
        
    def add_node(self, node) -> None:
        if isinstance(node, list):
            for nd in node:
                self.__check_same_data(nd)
                self.add_node(nd)
        else:
            if not isinstance(node, Node):
                self.__check_same_data(node)
                node = Node(node)
            parent = self.__find_place(node, self.root)
            if parent != node:
                node.parent = parent
                if node.data < parent.data:
                    parent.left = node
                elif node.data > parent.data:
                    parent.right = node

    def _del_with_child(self, node, child):
        par = node.parent
        child.parent = par
        node.parent = None
        if par.right == node:
            par.right = child
        else:
            par.left = child
        
    def find_min(self, root):
        if root.left == None:
            return root
        return self.find_min(root.left)
    
    def find(self, data, root = None) -> object:

        if not root:
            root = self.root
        if root.data == data:
            return root
        elif root.data < data and root.right != None:
            return self.find(data, root.right)
        elif root.data > data and root.left != None:
            return self.find(data, root.left)
        
    # доработать так чтобы при передаче числа находил узел дерева для удаления
    def delit(self, data) -> None:
        node = self.find(data)
        if not node:
            raise ValueError('Вершина отсутсвует в дереве')
        par = node.parent
        if node.right == None and node.left == None:
            if par.right == node:
                par.right = None
            elif node.parent.left == node:
                par.left = None
            node.parent = None
            del node
        elif node.right != None and node.left == None:
           self._del_with_child(node, node.right)
        elif node.left != None and node.right == None:
            self._del_with_child(node, node.left)
        else:
            ch = node.right
            if node.right == None:
                ch.parent = node.parent
                node.parent = None
                if par.right == node:
                    par.right = ch
                elif par.left == node:
                    par.left = ch
            else:
                mn = self.find_min(node)
                mn.data = node.data
                self._del_with_child(mn, mn.right)
            del node
    
    
    def show_tree(self, node = False):
        cash = []
        def inner(nd):
            if nd == False:
                nd = self.root
            if nd != None:
                cash.append(nd.data)
                inner(nd.left)
                inner(nd.right)
        inner(node)
        print(*cash)
    
    def __str__(self):
        return f'дерево с корнем {self.root.data}'
    
    # сравнивает по корню
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Tree):
            return self.root.data == __value.root.data
    
    def __lt__(self, __value: object) -> bool:
        if isinstance(__value, Tree):
            return self.root.data < __value.root.data
tree1 = Tree(10)
# tree2 = Tree(5)

# tree1.add_node(5)
# tree1.add_node(15)
tree1.add_node([5, 15, 1, 7, 3, 20])
# tree2.add_node([0, -4, -19, 21, 33, 2])
tree1.delit(7)
tree1.show_tree()
