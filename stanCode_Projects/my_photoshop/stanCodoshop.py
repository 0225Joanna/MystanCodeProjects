"""
File: stanCodoshop.py
Name: Joanna
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
This program removes people from the images.
"""

import os
import sys
import math
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    # Calculate the color distance of a pixel to the average RGB value.
    square_of_color_distance = (red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2
    color_distance = math.sqrt(square_of_color_distance)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    sum_of_red = 0      # Computing the sum of red pixels. Starting with 0.
    sum_of_green = 0    # Computing the sum of green pixels. Starting with 0.
    sum_of_blue = 0     # Computing the sum of blue pixels. Starting with 0.
    for i in range(len(pixels)):
        sum_of_red += pixels[i].red     # Adding new red pixel to the summary of all red pixels.
        sum_of_green += pixels[i].green     # Adding new green pixel to the summary of all green pixels.
        sum_of_blue += pixels[i].blue   # Adding new blue pixel to the summary of all blue pixels.
    avg_red = sum_of_red // len(pixels)     # Averaging red pixels
    avg_green = sum_of_green // len(pixels)     # Averaging green pixels
    avg_blue = sum_of_blue // len(pixels)       # Averaging blue pixels
    rgb = [avg_red, avg_green, avg_blue]    # return it as a list
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    rgb = get_average(pixels)       # Finding the average red, blue and green values of the given list.
    # Calculating the distance between the first pixel and a mean RGB value
    shortest_distance = get_pixel_dist(pixels[0], rgb[0], rgb[1], rgb[2])
    # At the beginning, assuming the first pixel as the best pixel(the closest color to the average).
    best_pixel = pixels[0]
    for i in range(len(pixels)):
        # Calculating the distance between a pixel and a mean RGB value
        distance = get_pixel_dist(pixels[i], rgb[0], rgb[1], rgb[2])
        if distance < shortest_distance:    # Comparing the distance with the shortest distance.
            # New distance is shorter. Reassigning the best pixel and shortest distance.
            best_pixel = pixels[i]
            shortest_distance = distance
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # -------For testing------------
    # green_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))

    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)
    # ----------------------------

    # Get pixels
    for x in range(width):
        for y in range(height):
            result_p = result.get_pixel(x, y)   # Getting the pixel of the blank.
            pixels = []
            for i in range(len(images)):
                img_p = images[i].get_pixel(x, y)   # Getting the pixel of the image.
                pixels.append(img_p)        # Listing the pixel of all the image.
            best_pixel = get_best_pixel(pixels)     # Getting the best pixel among all the images.
            # Assigning the pixel of the result picture.
            result_p.red = best_pixel.red
            result_p.green = best_pixel.green
            result_p.blue = best_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
