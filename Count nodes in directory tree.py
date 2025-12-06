def count_nodes(tree):
    name, children = tree
    total = 1
    for child in children:
        total += count_nodes(child)
    return total
