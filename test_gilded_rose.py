# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_item_quality_is_never_negative(self):
        items = [Item("Concert Stickers", 11, 0)]

        gildedRose = GildedRose(items)
        gildedRose.update_quality()

        self.assertEquals(0, items[0].quality)

    def test_quality_increments_in_backstage_more_than_10_days_for_sale(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 7)]

        gildedRose = GildedRose(items)
        gildedRose.update_quality()

        self.assertEquals(8, items[0].quality)

    def test_quality_increments_in_backstage_between_10_and_5_days_for_sale(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 7, 7)
        ]

        gildedRose = GildedRose(items)
        gildedRose.update_quality()

        self.assertEquals(9, items[0].quality)

    def test_quality_increments_in_backstage_less_than_6_days_for_sale(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 3, 7)
        ]

        gildedRose = GildedRose(items)
        gildedRose.update_quality()

        self.assertEquals(10, items[0].quality)

    def test_quality_to_0_after_sale_day_in_backstage(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 7)
        ]

        gildedRose = GildedRose(items)
        gildedRose.update_quality()

        self.assertEquals(0, items[0].quality)

    def test_quality_increments_in_aged_brie(self):
        items = [
            Item("Aged Brie", 2, 7)
        ]

        gildedRose = GildedRose(items)
        gildedRose.update_quality()

        self.assertEquals(8, items[0].quality)

    def test_double_increment_after_sale_day_aged_brie(self):
        items = [
            Item("Aged Brie", 0, 7)
        ]

        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        gildedRose.update_quality()

        self.assertEquals(11, items[0].quality)

    def test_quality_is_never_over_50(self):
        items = [
            Item("Aged Brie", 2, 50)
        ]

        gildedRose = GildedRose(items)
        gildedRose.update_quality()

        self.assertEquals(50, items[0].quality)

    def test_quality_should_always_be_80(self):
        items = [
            Item("Sulfuras, Hand of Ragnaros", 20, 80)
        ]

        gildedRose = GildedRose(items)
        gildedRose.update_quality()

        self.assertEquals(80, items[0].quality)

    def test_sale_day_should_never_change(self):
        items = [
            Item("Sulfuras, Hand of Ragnaros", 20, 80)
        ]

        gildedRose = GildedRose(items)
        gildedRose.update_quality()

        self.assertEquals(20, items[0].sell_in)

    def test_double_degradation_after_sale_day(self):
        items = [
            Item("Concert Stickers", 0, 7)
        ]

        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        gildedRose.update_quality()

        self.assertEquals(3, items[0].quality)

if __name__ == '__main__':
    unittest.main()
