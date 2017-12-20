from interface import Interface

class Priority_Queue(Interface):
    " Priority Queue Interface "
    def is_empty(self):
        " Checks whether Queue is empty "
        pass

    def insert(self, key):
        """
        Insert a key into Queue
        :param key:
        :return:
        """
        pass

    def min(self):
        """
        :return: the minimum element of the Queue
        """
        pass

    def replace_key(self,key,new_value):
        """
        Change the value of the key into new_value
        :param key: existing key
        :param new_value: the new_value of the key
        :return:
        """
        pass

    def extract_min(self):
        """
        Extracts the min
        :return:
        """
        pass