class AVL:

    class Node:
        def __init__(self,value,right=None,left=None,height = None):

            self.value = value
            self.right = right
            self.left = left
            self.height = height


    def __init__(self):

        self.__root  = None

    def remove(self,val):

        self.__root = self.__remove(self.__root,val)

    def insert(self,val):

        self.__root = self.__insert(self.__root,val) # insert the element


    def find(self,val):

        return self.__check_the_value(self.__root,val)

    def __str__(self):

        return self.__print_heights(self.__root)

    def height(self):

        return self.__get_height(self.__root)

    def min(self):

        if not self.is_empty():
            return self.__min(self.__root).value

    def max(self):

        if not self.is_empty():
            return self.__max(self.__root).value

    def __max(self,root):
        if root.right is None:
            return root
        else:
            return self.__max(root.right)


    def __check_the_value(self,node,val):
        if node is None:
            return False

        if node.value == val:
            return node
        elif val < node.value:
            return self.__check_the_value(node.left,val)
        else:
            return self.__check_the_value(node.right,val)

    def is_empty(self):
        return self.__root is None

    def __fix_height(self,node):

        node.height = max( self.__get_height(node.left), self.__get_height(node.right) ) + 1

    def __balance_factor(self,node):

        return self.__get_height(node.right) - self.__get_height(node.left)

    def __rotate_right(self,node):

        new_node = node.left
        node.left = new_node.right
        new_node.right = node
        self.__fix_height(node)
        self.__fix_height(new_node)

        return new_node

    def __rotate_left(self,node):
        new_node = node.right
        node.right = new_node.left
        new_node.left = node
        self.__fix_height(node)
        self.__fix_height(new_node)

        return new_node

    def __insert(self, root, val):

        if root is None:
            node = AVL.Node(val)
            node.height = 1
            return node

        if val < root.value:

            root.left = self.__insert(root.left, val)  # update the left subtree

        elif val > root.value:
            root.right = self.__insert(root.right, val)  # update the right subtree

        return self.__balance_tree(root)

    def __get_height(self,node):

        if node is None:
            return 0
        else:
            return node.height


    def __balance_tree(self,node):

        self.__fix_height(node)

        if self.__balance_factor(node) == 2:

            if self.__balance_factor(node.right) < 0:

                node.right = self.__rotate_right(node.right)

            return self.__rotate_left(node)


        if self.__balance_factor(node) == -2:

            if self.__balance_factor(node.right) > 0:

                node.left = self.__rotate_left(node.left)

            return self.__rotate_right(node)

        return node

    def __min(self,root):
        if root.left is None:
            return root
        else:
            return self.__min(root.left)

    def __remove_min(self,node):

        if node.left is None:
            node = node.right
            return node
        else:
            node.left = self.__remove_min(node.left)
            return self.__balance_tree(node)

    def __remove(self,node,value):

        if node:
            if value < node.value:
                node.left = self.__remove(node.left,value)
            elif value > node.value:
                node.right = self.__remove(node.right,value)
            else:
                if node.left is None or node.right is None:
                    if node.left:
                        node = node.left
                    else:
                        node = node.right
                else:
                    min_node = self.__min(node.right)
                    node.value = min_node.value
                    node.right = self.__remove_min(node.right)

            return self.__balance_tree(node)


    def __print_heights(self,node):

        if node is None:
            return ''
        string =  ','.join( [str(node.value),str(node.height),'\n'])
        string += self.__print_heights(node.left)
        string += self.__print_heights(node.right)
        return string


