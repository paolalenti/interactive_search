import os

def common_prefix(string_a, string_b):
    return os.path.commonprefix([string_a, string_b])


def construct_suffix_tree(string):
    tree = {}
    for i in range(len(string) + 1):
        suffix = string[i:] + "$"
        insert_suffix(suffix, tree)
    return tree


def insert_suffix(string, suffix_tree):
    if len(suffix_tree) == 0:
        suffix_tree[string] = []
        return suffix_tree

    found_match = False
    for key in list(suffix_tree.keys()):
        prefix = common_prefix(string, key)
        n = len(prefix)
        if len(prefix) > 0:
            found_match = True
            key_suffix = key[n:]
            string_suffix = string[n:]
            del suffix_tree[key]
            suffix_tree[prefix] = [key_suffix, string_suffix]

    if not found_match:
        suffix_tree[string] = []
    return suffix_tree


my_string = "banana"
print(construct_suffix_tree(my_string))

my_string = "ananas"
print(construct_suffix_tree(my_string))

my_string = "abrakadabra"
print(construct_suffix_tree(my_string))