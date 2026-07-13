import colorgram
rgb_colors = []
colors = cologram.extract('1jpg',30)
for color in colors:

  r= color.rgb.r
  b= color.rgb.b
  g= color.rgb.g

  new_color = (r,g,b)

  rgb_colors.append(new_color)

  print(rgb_colors)

''' #this will fetch a list of rgb tuples from the image '''
  
