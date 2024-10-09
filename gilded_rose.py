# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def __eq__(self, other):
        return self.name == other.name and self.sell_in == other.sell_in and self.quality == other.quality

class UpdateStrategy(ABC):
    @abstractmethod
    def update_quality(self, item):
        pass

class DefaultItemStrategy(UpdateStrategy):
    def update_quality(self, item):
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in <= 0 and item.quality > 0:
            item.quality -= 1

class AgedBrieStrategy(UpdateStrategy):
    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1
        if item.sell_in <= 0 and item.quality < 50:
            item.quality += 1

class BackstagePassStrategy(UpdateStrategy):
    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in <= 10 and item.quality < 50:
                item.quality += 1
            if item.sell_in <= 5 and item.quality < 50:
                item.quality += 1
        if item.sell_in <= 0:
            item.quality = 0

class ConjuredItemStrategy(UpdateStrategy):
    def update_quality(self, item):
        item.quality = max(item.quality - 2, 0)
        if item.sell_in <= 0:
            item.quality = max(item.quality - 2, 0)

class SulfurasStrategy(UpdateStrategy):
    def update_quality(self, item):
        pass  # Sulfuras never changes

class ItemUpdater:
    def __init__(self, strategy):
        self.strategy = strategy

    def update_quality(self, item):
        self.strategy.update_quality(item)
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1

class GildedRose:
    def __init__(self, items):
        self.items = items
        self.strategies = {
            "Aged Brie": ItemUpdater(AgedBrieStrategy()),
            "Backstage passes to a TAFKAL80ETC concert": ItemUpdater(BackstagePassStrategy()),
            "Sulfuras, Hand of Ragnaros": ItemUpdater(SulfurasStrategy()),
        }
        self.default_updater = ItemUpdater(DefaultItemStrategy())
        self.conjured_updater = ItemUpdater(ConjuredItemStrategy())

    def update_quality(self):
        for item in self.items:
            if item.name.startswith("Conjured"):
                self.conjured_updater.update_quality(item)
            else:
                updater = self.strategies.get(item.name, self.default_updater)
                updater.update_quality(item)