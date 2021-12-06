# import the file handling module
import os

from PIL import Image

# Creating a directory for the processed image
os.makedirs('watermarked_images')

 
# Storing the width and height of the logo
logo_image = Image.open('watermark_logo.png')
logo_image = logo_image.resize((50, 50))
logo_width, logo_height = logo_image.size

# Looping through images folder
for image in os.listdir('./images'):
    try:
    # Separting the filepath from the image's name
       path, filename = os.path.split(image)
       filename = os.path.splitext(filename)[0]
       

    #    Opening the image
       image = Image.open('./images/'+image)

    # Resizing the image to a set size
       edited_image = image.resize((300, 300))

    # setting the position for the placement
       width = edited_image.width
       height = edited_image.height

    # Using the paste function to postion the logo on the images
       edited_image.paste(logo_image, (width - logo_width, height - logo_height), logo_image)

    # Saving the images in the new directory
       edited_image.save('./watermarked_Images/' + filename + ".jpg")
    except IOError:
        print('error')
