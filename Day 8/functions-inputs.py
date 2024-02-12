import math 
def paint_calc(height, widht, cover):
    number_cans = math.ceil((height * widht) / cover)
    print(f"You'll need {number_cans} cans of paint")

wall_h = int(input("What's the height of the wall? "))
wall_w = int(input("What's the widht of the wall? "))
coverage = 5

paint_calc(height=wall_h, widht=wall_w, cover=coverage)

