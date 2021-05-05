from castle import Castle
from Globals import Globals
from path import PathFactory

castle2 = Castle(PathFactory().make_path1(), 50, 50, 200, Globals.castle_img)
print(castle2.health)
print(castle2)

castle3 = Castle(PathFactory().make_path3(), 500, 500, 400, Globals.castle_img)
print(castle3.health)
print(castle3)
