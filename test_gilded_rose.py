# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
  def test_quality_decreases_over_time(self):
    item_name = "Elixir of the Mongoose"
    sell_in = 0
    quality = 1
    items = [Item(item_name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    self.assertEquals(0, items[0].quality)

  def test_quality_of_brie_increases_over_time(self):
    item_name = "Aged Brie"
    sell_in = 0
    quality = 1
    items = [Item(item_name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    self.assertEquals(3, items[0].quality)

  def test_quality_of_tickets_increases_over_time(self):
    item_name = "Backstage passes to a TAFKAL80ETC concert"
    sell_in = 1
    quality = 1
    items = [Item(item_name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    self.assertEquals(4, items[0].quality)

  def test_quality_of_tickets_decreases_on_day_of_concert(self):
    item_name = "Backstage passes to a TAFKAL80ETC concert"
    sell_in = 0
    quality = 1
    items = [Item(item_name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    self.assertEquals(0, items[0].quality)


  def test_quality_decreases_faster_after_sellby_date(self):
    item_name = "Elixir of the Mongoose"
    sell_in = 0
    quality = 2
    items = [Item(item_name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    self.assertEquals(0, items[0].quality)

if __name__ == '__main__':
  unittest.main()
