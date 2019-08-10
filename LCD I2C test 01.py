# Displaying a logo

import machine
import framebuf

#----------------------------------------------------------

scl = machine.Pin('X9')
sda = machine.Pin('X10')
i2c = machine.I2C(scl=scl, sda=sda)

#----------------------------------------------------------
# Setting a buffer for the entire frame (64x32 pixels)
frame = framebuf.FrameBuffer(bytearray(64 * 32 // 8), 64, 32, framebuf.MONO_HLSB)

# Setting a buffer for the logo (28x16 pixels)
logo = framebuf.FrameBuffer(bytearray(28 * 16 // 8), 28, 16, framebuf.MONO_HLSB)

# Filling the logo with black (erasing everything/resetting)
logo.fill(0)

# Filling the entire logo area(28x16) with a white rectangle, starting at orgin 1, 1(x, y)
logo.fill_rect(1, 1, 28, 16, 1)

# Drawing a black 6px vertical line starting at 4, 1. And one at 4, 11
logo.vline(4, 1, 6, 0)
logo.vline(4, 11, 6, 0)

# Drawing a black 13x9 rectangle starting at 8, 4
logo.fill_rect(8, 4, 13, 9, 0)

# Drawing a black 6px vertical line starting at 24, 1. And one at 24, 11
logo.vline(24, 1, 6, 0)
logo.vline(24, 11, 6, 0)

#----------------------------------------------------------
# Filling the frame with black (erasing everything/resetting)
frame.fill(0)

# Putting the logo at position 18, 8 on the frame
frame.blit(logo, 18, 8)

# Writing the frame on the display? What's the 8 for? Check the docs!
i2c.writeto(8, frame)
