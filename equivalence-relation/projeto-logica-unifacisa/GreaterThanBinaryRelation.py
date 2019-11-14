#coding: utf-8

from BinaryRelation import BinaryRelation


class GreaterThanBinaryRelation(BinaryRelation):
    """A Binary Relation which elements in an ordered pair share the same first letter."""

    def contains_ordered_pair(self, x, y):
        return x > y
        pass

    def relation(self, S):
        """
        This method returns a set of pairs in SxS (a.k.a. S²) that belong to the binary relation.

        Arguments:
        S - The input set.

        Return a set of pairs in SxS (a.k.a. S²) that belong to the binary relation.
        """

        return set([(x, y) for x in S for y in S if self.contains_ordered_pair(x, y)])
        pass
