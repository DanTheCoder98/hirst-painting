import colorgram

colours = colorgram.extract("image.jpg", 50)

colour_palette = []

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b

    colour_palette.append((r, g, b))

print(colour_palette)