import Graphics.rectangle as re
import Graphics.circle as c
import Graphics.trd_graphics.cuboid as cb
import Graphics.trd_graphics.sphere as s
print("Rectangle")
print("Area:", re.area(4, 5))
print("Perimeter:", re.perimeter(4, 5))
print("Circle")
print("Area:", c.area(5))
print("Perimeter:", c.perimeter(5))
print("Cuboid")
print("Area:", cb.area(3, 4, 5))
print("Perimeter:", cb.perimeter(3, 4, 5))
print("Sphere")
print("Area:", s.area(4))
print("Perimeter:", s.perimeter(4))