from GRI.GildedRoseInn import GildedRoseInn
from GRI.agedbrieitem import AgedBrieItem
from GRI.backstagepassitem import BackstagePassItem
from GRI.commonitem import CommonItem
from GRI.conjureditem import ConjuredItem
from GRI.sulfurasitem import SulfurasItem

"""
Main application
"""

shop = GildedRoseInn()

commonItem = CommonItem(2, 25)
conjuredItem = ConjuredItem(15, 12)
agedBrieItem = AgedBrieItem(4, 5)
sulfurasItem = SulfurasItem()
backstagePassItem = BackstagePassItem(15, 20)


shop.add_item_in_slot(commonItem, 1)
shop.add_item_in_slot(conjuredItem, 41)
shop.add_item_in_slot(agedBrieItem, 13)
shop.add_item(sulfurasItem)
shop.add_item(backstagePassItem)

print("shop opens!")
print(shop)

for day in range(1, 30):
    print("shop after day " + str(day))
    shop.update_items()
    print(shop)
