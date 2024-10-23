import colorgram

image_colours = colorgram.extract("image.jpg", 1000)

colour_palette = []

for n in range(len(image_colours)):
    rgb_colours = image_colours[n].rgb.r, image_colours[n].rgb.g, image_colours[n].rgb.b
    colour_palette.append(rgb_colours)

print(colour_palette)