from drawer.tree import TreeDrawer
from data_structures.tree.node import Node


def iterative(pre_order, in_order):
    if len(pre_order) == 0:
        return None

    head = Node(pre_order[0])
    stack = [head]
    i = 1
    j = 0

    while i < len(pre_order):
        temp = None
        t = Node(pre_order[i])
        while stack and stack[-1].val == in_order[j]:
            temp = stack.pop()
            j += 1
        if temp:
            temp.right = t
        else:
            stack[-1].left = t
        stack.append(t)
        i += 1

    return head


def recursive(pre_order, in_order):
    if in_order:
        ind = in_order.index(pre_order.pop(0))
        root = Node(in_order[ind])
        root.left = recursive(pre_order, in_order[0:ind])
        root.right = recursive(pre_order, in_order[ind + 1:])
        return root


def _test(pre_order, in_order):
    if in_order:
        mid = in_order.index(pre_order[0])
        root = Node(pre_order.pop(0))
        root.left = _test(pre_order, in_order[:mid])
        root.right = _test(pre_order, in_order[mid + 1:])
        return root


if __name__ == '__main__':
    in_order = [4, 2, 5, 1, 6, 3, 7]
    pre_order = [1, 2, 4, 5, 3, 6, 7]
    # root = recursive(pre_order, in_order)
    root_ = _test(pre_order, in_order)
    # TreeDrawer().visualize(root)
    TreeDrawer().visualize(root_)
