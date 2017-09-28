#uses opencv. HowTo install :  http://docs.opencv.org/2.4/doc/tutorials/introduction/windows_install/windows_install.html
#import cv2

#vc = cv2.VideoCapture('testviews/2017-09-26.mp4')
#c=1

#if vc.isOpened():
#    rval , frame = vc.read()
#else:
#    rval = False

#while rval:
#    rval, frame = vc.read()
#    cv2.imwrite(str(c) + '.jpg',frame)
#    c = c + 1
#    cv2.waitKey(1)
#vc.release()
import numpy
from tkinter import *
from PIL import Image, ImageDraw


root = Tk()
root.geometry("800x600")
# read image as RGB and add alpha (transparency)
im = Image.open("ttest.jpg").convert("RGBA")

# convert to numpy (for convenience)
imArray = numpy.asarray(im)


def onCut():
    polygon = [(44,23),(623,243),(691,177),(581,26),(482,42)] #take from selected coordinates
    maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
    ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
    mask = numpy.array(maskIm)

    # assemble new image (uint8: 0-255)
    newImArray = numpy.empty(imArray.shape,dtype='uint8')

    # colors (three first columns, RGB)
    newImArray[:,:,:3] = imArray[:,:,:3]

    # transparency (4th column)
    newImArray[:,:,3] = mask*255

    # back to Image from numpy
    newIm = Image.fromarray(newImArray, "RGBA")
    newIm.save("out.png")



Button(root, text="cut", command=onCut).grid(column=2, row =0, sticky='NS', pady=4, padx=5)
mainloop()
# create mask
