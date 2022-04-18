from typing import Final

from GRI.item import Item


class CommonItem(Item):
    """
    Common item.
    """

    NAME: Final[str] = "Common"
    """
    Item name for Common item.
    """

    def __init__(self, sell_in: int, quality: int):
        """
        Creates a new common item instance, with given properties.

        :param sell_in: (int) sell in
        :param quality: (int) quality

        """
        super().__init__(CommonItem.NAME, sell_in, quality)

    def _update_quality(self) -> None:
        """
        Updates item quality.

        :return: (None)

        """
        self._quality -= 1
        if self.has_expired():
            self._quality -= 1
