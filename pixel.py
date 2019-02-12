# This example shows how to create a single pixel with a specific color channel
# order and blink it.
# Most NeoPixels = neopixel.GRB or neopixel.GRBW
# The 8mm Diffused NeoPixel (PID 1734) = neopixel.RGB
import time
import board
import neopixel

# Configure the setup
PIXEL_PIN = board.D18   # pin that the NeoPixel is connected to
ORDER = neopixel.RGBW   # pixel color channel order
WHITE = (100, 100, 100, 100) # color to blink
CLEAR = (0, 0, 0, 0)      # clear (or second color)
DELAY = 0.0          # blink rate in seconds
RED = (255, 0, 0, 0)
YELLOW = (255, 150, 0, 0)
GREEN = (0, 255, 0, 0)
CYAN = (0, 255, 255, 0)
BLUE = (0, 0, 255, 0)
PURPLE = (180, 0, 255, 0)

# Create the NeoPixel object
pixel = neopixel.NeoPixel(PIXEL_PIN, 60, pixel_order=ORDER)




# Loop forever and blink the color
while True:
    for i in range(60):
        # pixel[i] = WHITE
        # pixel[i-1] = RED
        # pixel[i-2] = CYAN
        # pixel[i-3] = PURPLE
        # pixel[i-4] = BLUE
        time.sleep(DELAY)
        pixel[i] = CLEAR
        time.sleep(DELAY)
