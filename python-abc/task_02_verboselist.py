#!/usr/bin/python3
"""
Module that creates a custom implementation of list.
"""


class VerboseList(list):
    """
    Custom list extension class.
    """
    def append(self, item, *rest):
        try:
            super().append(item)
        except Exception as error:
            print(error)
        print(f"Added [{item}] to the list.")
        for item_to_add in rest:
            try:
                super().append(item_to_add)
            except Exception as error:
                print(error)
            print(f"Added {item_to_add} to the list.")
        return None

    def extend(self, items):
        try:
            super().extend(items)
        except Exception as error:
            print(error)
        print(f"Extended the list with {len(items)} items.")
        return None

    def remove(self, item):
        try:
            super().remove(item)
        except Exception as error:
            print(error)
        print(f"Removed {item} from the list.")

    def pop(self, *index):
        if len(index) > 0:
            try:
                item_popped = super().pop(index[0])
            except Exception as error:
                print(error)
            print(f"Popped {item_popped} from the list.")
            return item_popped
        else:
            try:
                return super().pop()
            except Exception as error:
                print(error)




