"""
# Problem Set 5
# Name: Juan Rached
# Collaborators: Yongxin Shi
# Time: 5:00
"""    
from PIL import Image
import numpy

def make_matrix(color):
    """
    Generates a transformation matrix for the specified color.
    Inputs:
        color: string with exactly one of the following values:
               'red', 'blue', 'green', or 'none'
    Returns:
        matrix: a transformation matrix corresponding to
                deficiency in that color
    """
    # You do not need to understand exactly how this function works.
    if color == 'red':
        c = [[.567, .433, 0],[.558, .442, 0],[0, .242, .758]]
    elif color == 'green':
        c = [[0.625,0.375, 0],[ 0.7,0.3, 0],[0, 0.142,0.858]]
    elif color == 'blue':
        c = [[.95, 0.05, 0],[0, 0.433, 0.567],[0, 0.475, .525]]
    elif color == 'none':
        c = [[1, 0., 0],[0, 1, 0.],[0, 0., 1]]
    return c


def matrix_multiply(m1,m2):
    """
    Multiplies the input matrices.
    Inputs:
        m1,m2: the input matrices
    Returns:
        result: matrix product of m1 and m2
        in a list of floats
    """

    product = numpy.matmul(m1,m2)
    if type(product) == numpy.int64:
        return float(product)
    else:
        result = list(product)
        return result


def img_to_pix(filename):
    """
    Takes a filename (must be inputted as a string
    with proper file attachment ex: .jpg, .png)
    and converts to a list of representing pixels.

    For RGB images, each pixel is a tuple containing (R,G,B) values.
    For BW images, each pixel is an integer.

    # Note: Don't worry about determining if an image is RGB or BW.
            The PIL library functions you use will return the 
            correct pixel values for either image mode.

    Returns the list of pixels.

    Inputs:
        filename: string representing an image file, such as 'lenna.jpg'
        returns: list of pixel values 
                 in form (R,G,B) such as [(0,0,0),(255,255,255),(38,29,58)...] for RGB image
                 in form L such as [60,66,72...] for BW image
    """
    #Creates PIL.Image object using a file
    im = Image.open(filename)

    #Retrieves the pixels from the object as a list
    pixels = list(im.getdata())
    
    return pixels


def pix_to_img(pixels, size, mode):
    """
    Creates an Image object from a inputted set of RGB tuples.

    Inputs:
        pixels: a list of pixels such as the output of
                img_to_pixels.
        size: a tuple of (width,height) representing
              the dimensions of the desired image. Assume
              that size is a valid input such that
              size[0] * size[1] == len(pixels).
        mode: 'RGB' or 'L' to indicate an RGB image or a 
              BW image, respectively
    returns:
        img: Image object made from list of pixels
    """
    #Creates PIL.Image object with input mode and size (same as original)
    im = Image.new(mode,size)
    
    #Inputs pixels as the data for the image object created above
    im.putdata(pixels)
    
    return im


def filter(pixels, color):
    """
    pixels: a list of pixels in RGB form, such as 
            [(0,0,0),(255,255,255),(38,29,58)...]
    color: 'red', 'blue', 'green', or 'none', must be a string representing 
           the color deficiency that is being simulated.
    returns: list of pixels in same format as earlier functions,
    transformed by matrix multiplication
    """
    #Defines transform as the transformation matrix of the desired color 
    transform = make_matrix(color)
    
    #Create an empty list and an empty tuple to be used in the loop below
    cb_list = []
    cb_tuple = ()
    
    #This for loop takes each tuple in pixels and multiplies each element of it by
    #the transformation matrix defined above. It then adds each transformed element 
    #a new empty tuple and appends that tuple to the list. The tuple is emptied to 
    #repeat the process for each tuple in pixels. At the end a list containing all 
    #the tuples transformed by the matrix is returned.
    for tup in pixels:
         cb_pixels = matrix_multiply(transform, tup)
         for elem in cb_pixels:
             cb_tuple += (int(elem),)
         cb_list.append(cb_tuple)
         cb_tuple = ()
         
    return cb_list



def extract_end_bits(num_bits, pixel):
    """
    Extracts the last num_bits bits of each value of a given pixel. 

    example for BW pixel:
        num_bits = 5
        pixel = 214

        214 in binary is 11010110. 
        The last 5 bits of 11010110 are 10110.
                              ^^^^^
        The integer representation of 10110 is 22, so we return 22.

    example for RBG pixel:
        num_bits = 2
        pixel = (214, 17, 8)

        last 3 bits of 214 = 110 --> 6
        last 3 bits of 17 = 001 --> 1
        last 3 bits of 8 = 000 --> 0

        so we return (6,1,0)

    Inputs:
        num_bits: the number of bits to extract
        pixel: an integer between 0 and 255, or a tuple of RGB values between 0 and 255

    Returns:
        The last num_bits bits of pixel, as an integer (BW) or tuple of integers (RGB).
    """
    
    #The if statement below is to determine when we receive a tuple (RGB)
    #or an int (BW) for input, but the process is almost the same. 
    if isinstance(pixel, tuple):
        #Initialize lsb (which will contain our end bits) to zero
        #and create an empty tuple that will return an lsb for each
        #element in the input pixel tuple (three in the case of RGB).
        lsb = 0
        lsbTuple = ()
        
        #The for loop below searches through numbers of base 2.
        #Once it finds a number 2**n so that it divides a pixel element
        #it adds 2**(n-1) to lsb, the corresponding base two nuber. It then 
        #subtracts the same value from the original element, this is the equivalent 
        #to changing a binary value of 1 to a value of 0. Since all the numbers
        #behind this one are 0, if the remainding number is divisible by another
        #2**n number in the range of n, then that is another lsb and the process repeats.
        #This returns a tuple containing all lsb. The proccess is very similar for BW
        #pixels but the function returns an integer instead.
        
        for elem in pixel:
            for n in range(1,num_bits + 1): 
                if elem%(2**n) != 0:
                    lsb += 2**(n - 1)
                    elem -= 2**(n - 1)
            lsbTuple += (lsb,)
            lsb = 0
        return lsbTuple

    elif isinstance(pixel, int):
        lsb = 0
        for n in range(1,num_bits + 1): 
            if pixel%(2**n) != 0:
                lsb += 2**(n - 1)
                pixel -= 2**(n - 1)   
        return lsb
    
    else:
        print("ERROR: Invalid input for pixel")
    
            
            

def reveal_bw_image(filename):
    """
    Extracts the single LSB for each pixel in the BW input image. 
    Inputs:
        filename: string, input BW file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    #Open image file to obtain size
    im = Image.open(filename)
    size = im.size
    
    #Use img_to_pix() functin to get pixel data
    pixels = img_to_pix(filename)
    
    
    lsb = []
    #For loop uses function extract_end_bits to obtain
    #the last end bit of each pixel element. Each pixel
    #is then multiplied by 255 for greater contrast and 
    #appended to a list.
    for elem in pixels:
        lsb.append(255*extract_end_bits(1, elem))
    
    #Uses pix_to_img() function to get a PIL.Image object
    #from the list of pixels above and the size of the original image.
    secretIm = pix_to_img(lsb, size, 'L')
    
    return secretIm


def reveal_color_image(filename):
    """
    Extracts the 2 LSBs for each pixel in the RGB input image. 
    Inputs:
        filename: string, input RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    im = Image.open(filename)
    size = im.size
    
    pixels = img_to_pix(filename)

    #Essentially the same process as the reveal_bw_image()
    #function, but here I multiply each element of each tuple in 
    #pixels by 85 for better contrast and then add each to a new
    #tuple named scaledData. Then the list of scaled tuples is converted
    #into a PIL.Image object by the pix_to_img() function.
    
    lsb = []
    scaledData = ()
    for elem in pixels:
        rawData = extract_end_bits(2, elem)
        for elem in rawData:
            scaledData += (85*elem,)
        lsb.append(scaledData)
        scaledData = ()
    
    secretIm = pix_to_img(lsb, size, 'RGB')
    
    return secretIm

def reveal_image(filename):
    """
    Extracts the single LSB (for a BW image) or the 2 LSBs (for a 
    color image) for each pixel in the input image. Hint: you can
    use a function to determine the mode of the input image (BW or
    RGB) and then use this mode to determine how to process the image.
    Inputs:
        filename: string, input BW or RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """    
    im = Image.open(filename)
    if im.mode == '1' or im.mode == 'L':
        return(reveal_bw_image(filename))
    elif im.mode == 'RGB':
        return(reveal_color_image(filename))
    else:
        raise Exception("Invalid mode %s" % im.mode)


def main():
    pass

    # # Uncomment the following lines to test part 1

    im = Image.open('image_15.png')
    width, height = im.size
    pixels = img_to_pix('image_15.png')

    non_filtered_pixels = filter(pixels,'none')
    im = pix_to_img(non_filtered_pixels, (width, height), 'RGB')
    im.show()

    red_filtered_pixels = filter(pixels,'red')
    im2 = pix_to_img(red_filtered_pixels,(width,height), 'RGB')
    im2.show()

    # Uncomment the following lines to test part 2
    im = reveal_image('hidden1.bmp')
    im.show()
    
    im2 = reveal_image('hidden2.bmp')
    im2.show()


if __name__ == '__main__':
    main()

