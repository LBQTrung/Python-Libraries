from PIL import Image
import numpy as np
img = Image.open("Yasuo.jpg")

# To print format, size, mode:
print(img.format, img.size, img.mode)

# To display the image:
img.show()

new_img = img.convert("L")

# To save image
new_img.save("new_yasuo.jpg")
