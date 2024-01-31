def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [root] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(subtree):
    return not branches(subtree)


### Here are some examples to create a tree

# Fibonacci tree


def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        return tree(label(left) + label(right), [left, right])


def count_leaves(tree):
    """count the leaves of a tree"""
    if is_leaf(tree):
        return 1
    else:
        return sum(count_leaves(branch) for branch in branches(tree))


def leaves(tree):
    """Return a list containing the leaf labels of a tree

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """

    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(branch) for branch in branches(tree)], [])


def increment_leaves(T):
    """Return a tree like T but with leaf labels incremented"""
    if is_leaf(T):
        return tree(label(T) + 1)
    else:
        brchs = [increment_leaves(branch) for branch in branches(T)]
        return tree(label(T), brchs)


def increment(T):
    """Return a tree like T but with all labels incremented"""
    return tree(label(T) + 1, [increment(branch) for branch in branches(T)])


### Printing trees  


def print_tree(tree, indent=0):
    """indentation for better view---the indentation level corresponds to its depth"""
    print(" " * indent + str(label(tree)))
    for branch in branches(tree):
        print_tree(branch, indent + 1)
