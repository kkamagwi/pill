from PIL import Image
 
image = Image.open('python.jpg')
image.show()

cropped = image.crop((0, 80, 200, 400))
cropped.save('cropped_python.png')