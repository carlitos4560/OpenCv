import numpy as np
import cv2
import os

def gris(video):
    gris_bajo = np.array([0, 0, 100])
    gris_alto = np.array([200, 80, 175])
    mask_img_color = cv2.inRange(video, gris_bajo, gris_alto)
    return mask_img_color
# rangos de colores del fuego
#
#H
#

def maskBlue(video):
    frame = video
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(frame, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask=mask)
    return res

capture = cv2.VideoCapture('/home/carlitos/grafiOpenCV/feicobol/Carpeta sin título/escena0.mp4')

while (1):
    _, frame = capture.read()
    frame = cv2.resize(frame, (300,300))
    #cv2.imshow("frame",frame)
    #cv2.imshow("img_gabo   r", img_gabor)
    #rgb = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    video = gris(hsv)
    # video = maskBlue(hsv)
    kernel = np.ones((6, 6), np.uint8)  # las tres funciones ayudan a quitar el ruido
    mask = cv2.morphologyEx(video, cv2.MORPH_OPEN, kernel)
    blur = cv2.GaussianBlur(mask, (5, 5), 0)
    cany = cv2.Canny(blur, 1, 1)
    _, contours, _ = cv2.findContours(cany, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("mask", video)
    cv2.imshow("org", frame)


    cv2.imshow("hsv", hsv)
    # cv2.imshow("org", frame)
    cv2.imshow("blur", blur)
    cv2.imshow("cany", cany)
    # cv2.imshow('cont', contours)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
