import ctypes

#represents wallpaper on your computer which can be set

class Wallpaper:

    wallpapers = {"TOKYO": r'C:\Users\Melissa\Pictures\wallpapers\lofi aesthetic\tokyo street\tokyo street day.jpg',
                      "VIOLET": r'C:\Users\Melissa\Pictures\wallpapers\landscapes\violet evergarden.png'}

    def __init__(self):
        self.path = Wallpaper.wallpaper_dict["VIOLET"]

    def setWallpaper(self, path):
        self.path = path
        ctypes.windll.user32.SystemParametersInfoW(20, 0, self.path, 0)

    def getWallpaper(self):
        return self.path