# Problem Set 4A
# Name: Juan Rached
# Collaborators: Marissa Abbott
# Time Spent: 2:00
# Late Days Used: 0 used (Using 3 now)

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
example_tree = [[1,3],[[5,7],10]]

treeA = [[14,19],[[3,5],0]]
treeB = [[9,3],6]
treeC = [[7],[16,4,2],[8]]


# Part A1: Multiplication on tree leaves

def add_tree(tree):
    """
    Recursively computes the sum of all tree leaves.
    Returns an integer representing the product.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
    Outputs
       total: An int equal to the sum of all the leaves of the tree.

    """

    # TODO: Your code here
    
    #If list is empty return zero (base case of addition). Else,
    #if the first element of the tree is a list call the function again 
    #with the sublist, plus the remainding elements of the original list, as an argument 
    #If it is not a list simply add the first element to the remainding ones. If the first
    #element of the remainding ones is a list, repeat steps above.
    
    try:   
        if tree == []:
            return 0
        elif isinstance(tree[0], list): 
           return add_tree(tree[0]) + add_tree(tree[1:])
        else:
            return tree[0] + add_tree(tree[1:])
    except TypeError:
        print("Invalid tree")


# Part A2: Arbitrary operations on tree leaves

def sumem(a, b):
    """
    Example operator function.
    Takes in two integers, returns their sum.
    """
    return a + b


def prod(a, b):
    """
    Example operator function.
    Takes in two integers, returns their product.
    """
    return a * b


def op_tree(tree, op, base_case):
    """
    Recursively runs a given operation on tree leaves.
    Return type depends on the specific operation.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
       op: A function that takes in two inputs and returns the
       result of a specific operation on them.
       base_case: What the operation should return as a result
       in the base case (i.e. when the tree is empty).
    """

    # TODO: Your code here
    
    #In case list is empty, return base case.
    #Else, if the first element of the list is another list then take
    #that element as the list argument for the op_tree function (it does this until 
    #the first element of a sublist is not another list) and applies the operation
    #argument to the next element of the original list (unless that element is a 
    #sublist in which the recursive cycle repeats). Once a non-list element is found,
    #return the operation of that non-list with the next non-list element.
    
    if tree == []: 
        return base_case
    elif isinstance(tree[0], list): 
        return op(op_tree(tree[0], op, base_case), op_tree(tree[1:], op, base_case))
    else:
        return op(tree[0], op_tree(tree[1:], op, base_case))


# Part A3: Searching a tree

def search_greater_ten(a, b):
    """
    Operator function that searches for greater-than-10 values within its inputs.

    Inputs
        a, b: integers or booleans
    Outputs
        True if either input is equal to True or > 10, and False otherwise
    """

    # TODO: Your code here
    
    #Checks whether a and b are bools, ints or a convenation of 
    #the two and returns true if either of them is true or greater than 10.
    if isinstance(a, bool) and isinstance(b, bool):
        if a or b:
            return True
        else: 
            return False
    elif isinstance(a, int) and isinstance(b, bool):
        if a > 10 or b:
            return True
        else:
            return False
    elif isinstance(a, bool) and isinstance(b, int):
        if a or b > 10:
            return True
        else:
            return False
    elif isinstance(a, int) and isinstance(b, int):
        if a > 10 or b > 10:
            return True
        else:
            return False

# Part A4: Find the maximum element of a tree using op_tree and max() in the
# main function below (remembering to pass the function in without parenthesis)
if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below.
    print(op_tree(treeA, max, 0))
    
    pass
