# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np

def getTextOverlay(input_image):
    img_bw = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)    
    a,thresh = cv2.threshold(img_bw,12,255,cv2.THRESH_BINARY)
    output = cv2.boxFilter(thresh,0,(5,5),normalize=False)
    return output

    
    

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    cv2.imshow("input",image)
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)