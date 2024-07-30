import colorgram
# Extract 10 colors from an image.
colors = colorgram.extract('image.jpg', 10)

color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))

print(color_list)
