import math

r, a = map(int, input().split())

print(f"Длина окружности: {round(2*math.pi*r, 2)}. Площадь круга составляет {round(math.pi*r**2/a**2*100, 2)}% от площади квадрата")