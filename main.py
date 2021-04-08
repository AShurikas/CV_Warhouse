from PIL import Image

infile1 = 'Got_order.png'
infile2 = 'Empty_order.png'


def compare_pixels(image1, image2, pixel_coordinates=(114, 231)):

    """image1, 2 - input opened images
        *pixel_coordinates - 4 arguments x1, y1, x2, y2 """
    with Image.open(image1) as img1:
        with Image.open(image2) as img2:
            pix1 = img1.load()
            pix2 = img2.load()
    return pix1[pixel_coordinates] == pix2[pixel_coordinates]


print(compare_pixels(infile1, infile2))
