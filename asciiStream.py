# curses and CV2
import curses
import cv2
from curses import wrapper

#variables
scale = 0.1 # higher up the scale the more we may need to zoom out

def main(screen):
        
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        raise IOError("I cant catch the webcam stream boss")
    while True:
        ret, frame = capture.read()
        frame = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA) # lets play with these values later to try and make it more detailed
        width = len(frame[0])*2 # we do this because the ASCII characters are twice as tall as they are wide.
        #convert the frame to grayscale (0-255)
        gscale = []
        for i, b in enumerate(frame):
            for x, a in enumerate(b):
                    sum = a[0]+a[1]+a[2]
                    sum /= 3
                    sum = int(sum)
                    gscale.append(sum)
                    gscale.append(sum)

        #convert the grayscale to ASCII
        chars = ["@", "#", "S", "%", "?", "+", "=", "-", ":", ",", ".", " " ]
        chars.reverse()
        asciiPx = [chars[pixel//25] for pixel in gscale]
        asciiPx = "".join(asciiPx)
        asciiFrame = [asciiPx[i:i+width] for i in range(0, len(asciiPx), width)]
        #display image in terminal
        for l, x in enumerate(asciiFrame):
            try:
                screen.addstr(l, 0, x)
            except:
                pass
        screen.refresh()

    capture.release()
    return


wrapper(main)