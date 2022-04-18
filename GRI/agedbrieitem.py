from typing import Final

from GRI.item import Item


class AgedBrieItem(Item):
    """
    Aged brie item.
    """

    NAME: Final[str] = "Aged Brie"
    """
    Item name for Aged Brie.
    """

    def __init__(self, sell_in: int, quality: int):
        """
        Creates a new aged brie item instance, with given properties.

        :param sell_in: (int) sell in

        :param quality: (int) quality

        """
        super().__init__(AgedBrieItem.NAME, sell_in, quality)

    def _update_quality(self) -> None:
        """
        Updates item quality.

        :return: (None)

        """
        self._quality += 1
        if self.has_expired():
            self._quality += 1
