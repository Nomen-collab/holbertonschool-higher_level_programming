"""
This module defines a custom iterator class `CountedIterator`
that extends the built-in iterator.

Classes:
    CountedIterator: A custom iterator that counts the number
    of items iterated over.
"""


class CountedIterator:
    """
    A custom iterator that counts the number of items iterated over.

    Methods:
        get_count: Returns the current count of iterated items.
    """

    def __init__(self, iterable):
        """
        Initialize a new CountedIterator instance.

        Args:
            iterable: The iterable to be wrapped by the CountedIterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            CountedIterator: The iterator object.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.

        Returns:
            The next item from the iterator.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Return the current count of iterated items.

        Returns:
            int: The count of iterated items.
        """
        return self.count
