class BinarySearchTree:

    class Node:
        def __init__(self,value,right=None,left=None):
            self.value = value
            self.right = right
            self.left = left

    def __init__(self):
        self.__root = None
        self.count = 0

    def is_empty(self):
        return self.__root is None

    def __insert(self,root, val):

        if root is None:
            return BinarySearchTree.Node(val)

        if val < root.value:

            root.left = self.__insert(root.left,val) # update the left subtree
        else:
            root.right = self.__insert(root.right,val) # update the right subtree

        return root

    def __check_the_value(self,node,val):
        if node is None:
            return False

        if node.value == val:
            return node
        elif val < node.value:
            return self.__check_the_value(node.left,val)
        else:
            return self.__check_the_value(node.right,val)

    def check_if_exist(self,val):
        if self.__check_the_value(self.__root,val):
            return True
        else:
            return False

    def insert(self,val):
        self.count +=1
        self.__root = self.__insert(self.__root,val)

    def find(self,val):
        return self.__check_the_value(self.__root,val)

    def __min(self,root):
        if root.left is None:
            return root
        else:
            return self.__min(root.left)

    def min(self):

        if not self.is_empty():
            return self.__min(self.__root).value

    def __max(self,root):
        if root.right is None:
            return root
        else:
            return self.__max(root.right)

    def max(self):

        if not self.is_empty():
            return self.__max(self.__root).value

    def __repr__(self):
        return "BinarySearchTree.Node(" + repr(self.__root.value) + "," + repr(self.__root.left) + "," + repr(self.__root.right)+ ")"

    def __str__(self):
        return "BinarySearchTree(" + str(self.__root) + ")"

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
                    min_node = min_node.right
            return node

    def remove(self,value):
        self.count -=1
        self.__remove(self.__root,value)

    def __print_f(self, node,depth=0):
        ret = ""
        if node is None:
            return ret
        # Print right branch
        if node.right != None:
            ret += self.__print_f(node.right,depth+1)

        # Print own value
        ret += "\n" + ("  " * depth) + str(node.value)

        # Print left branch
        if node.left != None:
            ret += self.__print_f(node.left,depth+1)

        return ret
    def __traverse_in_order(self,root):
        result = []
        if root is None:
            return ''
        else:
            result.append(self.__traverse_in_order(root.left))
            result.append(root.value)
            result.append(self.__traverse_in_order(root.right))
            result  = filter(None,result)
        return ','.join(str(i) for i in result)

    def traverse_in_order(self):
        return self.__traverse_in_order(self.__root)

    def __traverse_in_preorder(self,root):
        result = []
        if root is None:
            return ''
        else:
            result.append(root.value)
            result.append(self.__traverse_in_order(root.left))
            result.append(self.__traverse_in_order(root.right))
            result  = filter(None,result)
        return ','.join(str(i) for i in result)

    def traverse_in_preorder(self):
        return self.__traverse_in_preorder(self.__root)

    def __traverse_in_postorder(self, root):
        result = []
        if root is None:
            return ''
        else:
            result.append(self.__traverse_in_order(root.left))
            result.append(self.__traverse_in_order(root.right))
            result.append(root.value)
            result = filter(None, result)
        return ','.join(str(i) for i in result)

    def traverse_in_postorder(self):
        return self.__traverse_in_postorder(self.__root)

    def __str__(self):
        return self.__print_f(self.__root)

    def __check_bst(self,root):

        result = True
        if root:
            if root.left:
                result = result and root.value>root.left.value and self.__check_bst(root.left)
            if root.right:
                result = result and root.value<=root.right.value and self.__check_bst(root.right)

        return  result

    def check_bst(self):
        return self.__check_bst(self.__root)





