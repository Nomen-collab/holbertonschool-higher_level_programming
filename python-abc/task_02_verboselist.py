"""
This module defines a custom list class `VerboseList` that
extends the built-in list class.

Classes:
    VerboseList: A custom list class that prints
    notifications for certain operations.
"""


class VerboseList(list):
    """
    A custom list class that prints notifications
    for certain operations.

    Methods:
        append: Append an item to the list and print
        a notification.
        extend: Extend the list by appending elements
        from the iterable and print a notification.
        remove: Remove the first occurrence of an item
        from the list and print a notification.
        pop: Remove and return the item at the given
        index and print a notification.
    """

    def append(self, item):
        """
        Append an item to the list and print a notification.

        Args:
            item: The item to append.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list by appending elements from the
        iterable and print a notification.

        Args:
            iterable: An iterable with elements to add.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of an item from the
        list and print a notification.

        Args:
            item: The item to remove.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return the item at the given index and
        print a notification.

        Args:
            index (int, optional): The index of the item to
            remove. Defaults to -1 (the last item).

        Returns:
            The removed item.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
