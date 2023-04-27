import unittest
#from wallpaper import TOKYO_WALLPAPER, Wallpaper
import wallpaper

class Test(unittest.TestCase):
    def test_changeWallpaper(self):
        wallpaper = Wallpaper()
        wallpaper.setWallpaper(Wallpaper.wallpaper_dict["VIOLET"])


