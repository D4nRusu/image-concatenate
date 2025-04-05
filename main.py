from PIL import Image, ImageDraw, ImageFont

template = Image.open("template.jpeg")

before_img = Image.open("bf.jpeg")
after_img = Image.open("af.jpeg")

slotx = 790
sloty = 1054
pos = 811

before_resized = before_img.resize((slotx, sloty))
after_resized = after_img.resize((slotx, sloty))

template.paste(before_resized, (0,0))
template.paste(after_resized, (pos,0))

template.save("output.jpeg")