from typing import Final

from GRI.item import Item


class GildedRoseInn:
    """
    GildedRose Inn shop.
    """

    SIZE: Final[int] = 42
    """
    Shop size.
    """

    def __init__(self):
        """
        Creates a new GildedRose Inn shop instance (empty).
        """
        self._items = [None]*GildedRoseInn.SIZE
        self._count = 0

    def __str__(self) -> str:
        """
        Exports shop as a string.

        :return: (str) a multiline string representing the shop (one item per line)

        """
        result = ""
        for slot in range (GildedRoseInn.SIZE):
            if not self._is_slot_empty(slot):
                result += "slot " + str(slot) + " -> "
                result = result + str(self._items[slot]) + "\n"
        return result

    def add_item_in_slot(self, item: Item, slot: int) -> bool:
        """
        Adds item in given slot.

        :param item: (Item) item to add
        :param slot: (int) slot number

        :return: (bool) True if item has been added in slot, False if it wasn't possible

        """
        if slot < 0 or slot >= GildedRoseInn.SIZE:
            return False
        if not self._is_slot_empty(slot):
            return False
        self._items[slot] = item
        self._count += 1
        return True

    def add_item(self, item: Item) -> bool:
        """
        Adds item, in first empty slot.

        :param item: (Item) item to add

        :return: (bool) True if item has been added in slot, False if not empty slot was found

        """
        if self._count == GildedRoseInn.SIZE:
            return False
        for slot in range(GildedRoseInn.SIZE):
            if self._is_slot_empty(slot):
                self._items[slot] = item
                self._count += 1
                break
        return True

    def _is_slot_empty(self, slot: int) -> bool:
        """
        Checks if a given slot is empty.

        :param slot: (int) slot number

        :return: (bool) True if slot is empty, False else

        """
        return self._items[slot] is None

    def update_items(self) -> None:
        """
        Updates all items.

        :return: (None)

        """
        for slot in range(GildedRoseInn.SIZE):
            if not self._is_slot_empty(slot):
                self._items[slot].update()
