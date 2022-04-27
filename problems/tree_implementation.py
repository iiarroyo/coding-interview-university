from bisect import insort_right


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data > self.data:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)

        if data < self.data:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)
    def get_node_count(self):
        count = 1
        if self.left:
            count += self.left.get_node_count()
        if self.right:
            count += self.right.get_node_count()
        return count

    def print_values(self):
        if self.left:
            self.left.print_values()
        print(self.data)
        if self.right:
            self.right.print_values()

    def in_tree(self, value):
        if self.data == value:
            return True
        elif value > self.data:
            if self.right:
                return self.right.in_tree(value)
        elif value < self.data:
            if self.left:
                return self.left.in_tree(value)
        return False
        
    def get_height(self):
        l_height, r_height = 1, 1
        if self.left:
            l_height += self.left.get_node_count()
        if self.right:
            r_height += self.right.get_node_count()
        return max(l_height, r_height)

    def get_min(self):
        if self.left:
            return self.left.get_min()
        return self.data

    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.data

    def is_binary_search_tree(self):
        res = True
        if self.left:
            if not self.left.data < self.data:
                return False
        if self.right:
            if self.right.data > self.data:
                return False
        res &= self.left.is_binary_search_tree()
        res &= self.right.is_binary_search_tree()
        return res
    
    def delete_value(self, value):
        if self.data == value:
            if self.left and self.right:
                new_val = self.left.get_max()
            elif self.left:
                self.data = self.left.data
                self.left = self.left.left
                self.right = self.left.right
            elif self.right:
                self.data = self.left.data
                self.left = self.left.left
                self.right = self.left.right

        elif value > self.data:
            if self.right:
                return self.right.in_tree(value)
        elif value < self.data:
            if self.left:
                return self.left.in_tree(value)
        return False


if __name__ == "__main__":
    root = Node(1)
    root.insert(0)
    root.insert(10)
    root.insert(20)
    root.insert(30)
    root.insert(25)

    print(root.get_min())
        
