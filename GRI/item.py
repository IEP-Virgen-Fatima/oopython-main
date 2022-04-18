from abc import ABCMeta, abstractmethod
from typing import Final


class Item(metaclass=ABCMeta):
    """
    Item (abstract class)
    """

    MIN_QUALITY: Final[int] = 0
    """
    Quality lower bound.
    """

    MAX_QUALITY: Final[int] = 50
    """
    Quality upper bound.
    """

    def __init__(self, name: str, sell_in: int, quality: int):
        """
        Creates a new item instance, with given properties.

        :param name: (str) name
        :param sell_in: (int) number of days remaining before expiration
        :param quality: (int) quality

        """
        self._name = name
        self._sell_in = sell_in
        self._quality = quality

    def __str__(self) -> str:
        """
        Exports item as a string.

        :return: (str) a string representing the item

        """
        return self._name + " Item (" \
               + str(self._quality) \
               + "," + str(self._sell_in) \
               + ")"

    @property
    def name(self) -> str:
        """
        Returns name.

        :return: (str) name

        """
        return self._name

    @property
    def sell_in(self) -> int:
        """
        Returns sell in.

        :return: (int) sell in

        """
        return self._sell_in

    @property
    def quality(self) -> int:
        """
        Returns quality.

        :return: (int) quality

        """
        return self._quality

    def has_expired(self) -> bool:
        """
        Checks if item has expired.

        :return: (bool) True if item has expired, False else

        """
        return self._sell_in <= 0

    def update(self) -> None:
        """
        Updates item.

        :return: (None)

        """
        self._update_sell_in()
        self._update_quality()
        self._ensure_quality_remains_in_bounds()

    @abstractmethod
    def _update_quality(self) -> None:
        """
        Updates item quality.

        :return: (None)

        """
        pass

    def _update_sell_in(self) -> None:
        """
        Updates item sell in.

        :return: (None)

        """
        self._sell_in -= 1

    def _ensure_quality_remains_in_bounds(self) -> None:
        """
        Ensures quality remains in bounds.

        :return: (None)

        """
        if self._quality < Item.MIN_QUALITY:
            self._quality = Item.MIN_QUALITY

        if self._quality > Item.MAX_QUALITY:
            self._quality = Item.MAX_QUALITY
