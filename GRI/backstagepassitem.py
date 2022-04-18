from typing import Final

from GRI.item import Item


class BackstagePassItem(Item):
    """
    Backstage pass item.
    """

    NAME: Final[str] = "Backstage Pass"
    """
    Item name for Backstage Pass.
    """

    FIRST_THRESHOLD: Final[int] = 10
    """
    First threshold (in days).
    """

    SECOND_THRESHOLD: Final[int] = 5
    """
    Second threshold (in days).
    """

    def __init__(self, sell_in: int, quality: int):
        """
        Creates a new backstage pass item instance, with given properties.

        :param sell_in: (int) sell in
        :param quality: (int) quality

        """
        super().__init__(BackstagePassItem.NAME, sell_in, quality)

    def _update_quality(self) -> None:
        """
        Updates item quality.

        :return: (None)

        """
        if self.has_expired():
            self._quality = Item.MIN_QUALITY
            return
        self._quality += 1
        if self._sell_in <= BackstagePassItem.FIRST_THRESHOLD:
            self._quality += 1
        if self._sell_in <= BackstagePassItem.SECOND_THRESHOLD:
            self._quality += 1
