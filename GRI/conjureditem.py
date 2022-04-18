from typing import Final

from GRI.item import Item


class ConjuredItem(Item):
    """
    Conjured item.
    """

    NAME: Final[str] = "Conjured"
    """
    Item name for Conjured.
    """

    def __init__(self, sell_in: int, quality: int):
        """
        Creates a new conjured item instance, with given properties.

        :param sell_in: (int) sell in
        :param quality: (int) quality

        """
        super().__init__(ConjuredItem.NAME, sell_in, quality)

    def _update_quality(self) -> None:
        """
        Updates item quality.

        :return: (None)

        """
        self._quality -= 2
        if self.has_expired():
            self._quality -= 2
