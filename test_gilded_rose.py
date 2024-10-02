# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
    
    def test_backstage_passes_quality_increases(self):
        backstage = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(backstage, 15, 20), Item(backstage, 10, 49), Item(backstage, 5, 49)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(gr.items, [Item(backstage, 14, 21), Item(backstage, 9, 50), Item(backstage, 4, 50)])
    
    def test_conjured_items_degrade_twice_as_fast(self):
        conjured = "Conjured Mana Cake"
        items = [Item(conjured, 3, 6)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(gr.items, [Item(conjured, 2, 4)])

    def test_quality_never_negative(self):
        elixir = "Elixir of the Mongoose"
        items = [Item(elixir, 0, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(gr.items, [Item(elixir, -1, 0)])

if __name__ == '__main__':
    unittest.main()
