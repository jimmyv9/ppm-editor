'''
 * Program or Lab 8: Extra Credit PPM Viewer
 *
 * Programmer: João Veloso
 *
 * Due Date: December 7, 2016
 *
 * COMP141, Fall 2016
 *
 * Pledge: I have neither given nor received unauthorized aid
 *         on this program. 
 *
 * Description: Module with functions used to alter images
 *
 * Input: No user input, takes input from in_file
 *
 * Output: Generally outputs RGB values to generate image
 *
'''

#averages values to create gray_scale
def gray_scale(r, g, b, max_color):
    gray = round((int(r) + int(g) + int(g))/3)
    r = gray
    g = gray
    b = gray
    return r, g, b

#flips image along horizontal axis (not functioning properly)
def flip_horizontal(in_file, width):
    newline = []
    reversedlist = []
    for line in in_file:
        newline.append(line)
        if len(newline) == width:
            for pixel in reversed(newline):
                reversedlist.append(pixel)
            newline.clear()
            return reversedlist

#setting values of respective colors to 0
def flatten_red(r, g, b, max_color):
    return 0, g, b

def flatten_green(r, g, b, max_color):
    return r, 0, b

def flatten_blue(r, g, b, max_color):
    return r, g, 0

#setting RGB values to zero with each negate function         
def negate_red(r, g, b, max_color):
    return max_color - int(r), g, b

def negate_green(r, g, b, max_color):
    return r, max_color - int(g), b
    
def negate_blue(r, g, b, max_color):
    return r, g, max_color - int(b)
