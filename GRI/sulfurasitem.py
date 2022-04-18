from typing import Final

from GRI.item import Item


class SulfurasItem(Item):
    """
    Sulfuras item.
    """

    NAME: Final[str] = "Sulfuras"
    """
    Item name for Sulfuras.
    """

    SELL_IN: Final[int] = 1
    """
    Sell in (sulfuras nevers expires).
    """

    QUALITY: Final[int] = 80
    """
    Quality (sulfuras is legendary).
    """

    def __init__(self):
        """
        Creates a new sulfuras item instance.

        """
        super().__init__(SulfurasItem.NAME, SulfurasItem.SELL_IN, SulfurasItem.QUALITY)

    def update(self) -> None:
        """
        Updates item.

        :return: (None)

        """
        pass

    def _update_quality(self) -> None:
        """
        Updates item quality.

        :return: (None)
        """
        pass
