import cv2
import numpy as np

# Create a function based on a CV2 Event (Left button click)
drawing = False  # True if mouse is pressed
ix, iy = -1, -1


# mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        # When you click DOWN with left mouse button drawing is set to True
        drawing = True
        # Then we take note of where that mouse was located
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        # Now the mouse is moving
        if drawing == True:
            # If drawing is True, it means you've already clicked on the left mouse button
            # We draw a rectangle from the previous position to the x,y where the mouse is
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)


    elif event == cv2.EVENT_LBUTTONUP:
        # Once you lift the mouse button, drawing is False
        drawing = False
        # we complete the rectangle.
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)


# Create a black image
img = np.zeros((512, 512, 3), np.uint8)
# This names the window so we can reference it
cv2.namedWindow(winname='my_drawing')
# Connects the mouse button to our callback function
cv2.setMouseCallback('my_drawing', draw_rectangle)

while True:  # Runs forever until we break with Esc key on keyboard
    # Shows the image window
    cv2.imshow('my_drawing', img)

    # CHECK TO SEE IF ESC WAS PRESSED ON KEYBOARD
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()