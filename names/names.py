import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BinarySearchTree(value)
        if value < self.value and self.left is None:
            self.left = new_node
        elif value < self.value:
            self.left.insert(value)
        elif value >= self.value and self.right is None:
            self.right = new_node
        elif value >= self.value:
            self.right.insert(value)
        else:
            return None

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value and self.right is not None:
            return self.right.contains(target)
        elif target < self.value and self.left is not None:
            return self.left.contains(target)
        else:
            return False


names_bst = BinarySearchTree(names_1[0])
for name_1 in names_1[1:]:
    names_bst.insert(name_1)
for name_2 in names_2:
    if names_bst.contains(name_2) is not False:
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
