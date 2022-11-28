from PIL import Image, ImageEnhance
import os

image_name = input('File Name: ')
image_thumbnail = "media/" + os.path.splitext(image_name)[0] + ".thumbnail"

def get_thumbnail(image_name):
    with Image.open(image_name) as im:
        width, height = im.size
        if im.mode in ("RGBA", "P"):
             im = im.convert("RGB")

        if width < height: # If is a portait type image

            size = (1080,1080) # Different dimensions

            if width < 1080: # Preventing image to be stretch out.
                size = (1080,width)


            im.thumbnail(size, Image.LANCZOS, reducing_gap=1.0)
            im = ImageEnhance.Contrast(im)

            im.enhance(1.3).save(image_thumbnail, "JPEG") # Add contrast and save.

            return "Done - Portait" # return the url.

        if height < 1080: # Preventing image to be stretch out.
            size = (1920,height)


        im.thumbnail(size, Image.LANCZOS, reducing_gap=1.0)
        im = ImageEnhance.Contrast(im)

        im.enhance(1.3).save(image_thumbnail, "JPEG") # Add contrast and save.

        return  "Done - Normal" # return url.

print(get_thumbnail(image_name))
