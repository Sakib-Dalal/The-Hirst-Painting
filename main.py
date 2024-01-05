import colorgram
""" for more info about colorgram visit link:- https://pypi.org/project/colorgram.py/"""

color = colorgram.extract("image.jpg", 30)

my_colors_list = []

for i in range(len(color)):
    my_tuple_rgb = (color[i].rgb.r, color[i].rgb.g, color[i].rgb.b)
    my_colors_list.append(my_tuple_rgb)

print(my_colors_list)
