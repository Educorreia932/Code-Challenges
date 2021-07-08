def find_parent_node(h, n):
    current_node = 2 ** h - 1
    parent_node = -1
    h -= 1

    while current_node != n:
        parent_node = current_node
        left_node = current_node - 2 ** h
        right_node = current_node - 1

        if n <= left_node:
            current_node = left_node

        else:
            current_node = right_node

        h -= 1

    return parent_node

def solution(h, q):
    return [find_parent_node(h, n) for n in q]
