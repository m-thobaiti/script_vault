from PIL import Image
 # actually called Pillow when installing, image manipulation import

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."] 
# symbols based on the level of grayscale in the modified image

def resize_img(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)
# resizes image based on the input(100), self-explanatory calculations beyond that


def grayscale(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
# turns the image into grayscale, L for Luminance

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

# takes the image data as a data tuple (in the case of grayscale, that would look like:
#53
#53
#53
#53 
#53
# each number above is 1 pixel from image.getdata()

# based on the image input, you could end up with a lot of data, the example image used had 160000 pixels in total

# the .join takes all the available pixel data, divided by 25 since we only have 11 "levels" of ascii characters and returns the result as a string
# this works with every potential level (up to 255) because the result is always an integer

def main(new_width=100):
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        return
  
    new_img_data = pixels_to_ascii(grayscale(resize_img(image)))
    
    pixel_count = len(new_img_data)  
    ascii_image = "\n".join([new_img_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    print(ascii_image)
    
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
 
main()