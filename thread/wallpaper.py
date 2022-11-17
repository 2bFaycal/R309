#mettre un fond decran sur le bureau windows 10

import ctypes
import os

SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDWININICHANGE = 0x02

def set_wallpaper(path):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
    
def get_wallpaper():
    return os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Packages', 'Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy', 'LocalState', 'Assets')

def main():
    wallpaper = get_wallpaper()
    for file in os.listdir(wallpaper):
        if file.endswith('.jpg'):
            set_wallpaper(os.path.join
(wallpaper, file))
            break

if __name__ == '__main__':
    main()
