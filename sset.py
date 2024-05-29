#!/usr/bin/env python3

"""
Suffix tree to search in dictionary
"""

from typing import List
from suffix_tree import Tree


class SSet:
    """String set. Should be based on Suffix tree"""

    def __init__(self, fname: str) -> None:
        """Saves filename of a dictionary file"""
        self.fname = fname
        self.words = None

    def load(self) -> None:
        """
        Loads words from a dictionary file.
        Each line contains a word.
        File is not sorted.
        """
        with open(self.fname, 'r') as f:
            self.words = [line.rstrip() for line in f]
            self.d = {}
            for i in range(len(self.words)):
                self.d[str(i)] = self.words[i]
            self.tree = Tree(self.d)


    def search(self, substring: str) -> List[str]:
        """Returns all words that contain substring."""
        res = set()
        for id_, path in self.tree.find_all(substring):
            res.add(self.d[id_])
        # words_old = [w for w in self.words if substring in w]
        return list(res)
