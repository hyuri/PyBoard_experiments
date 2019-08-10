# Logo animation

import machine
import framebuf
from time import sleep_ms

#----------------------------------------------------------

scl = machine.Pin('X9')
sda = machine.Pin('X10')
i2c = machine.I2C(scl=scl, sda=sda)

#----------------------------------------------------------
# Setting a buffer for the entire frame (64x32 pixels)
frame = framebuf.FrameBuffer(bytearray(64 * 32 // 8), 64, 32, framebuf.MONO_HLSB)

# Setting a buffer for the logo, and one for a color-inverted version of the logo
logo = framebuf.FrameBuffer(bytearray(29 * 16 // 8), 29, 16, framebuf.MONO_HLSB)
logo_inverted = framebuf.FrameBuffer(bytearray(29 * 16 // 8), 29, 16, framebuf.MONO_HLSB)

# Logo
logo.fill(0)
logo.fill_rect(0, 0, 29, 16, 1)

logo.vline(3, 0, 6, 0)
logo.vline(3, 10, 6, 0)

logo.fill_rect(7, 3, 15, 10, 0)

logo.vline(14, 0, 16, 0)

logo.vline(25, 0, 6, 0)
logo.vline(25, 10, 6, 0)

# Logo inverted
logo_inverted.fill(1)
logo_inverted.fill_rect(0, 0, 29, 16, 0)

logo_inverted.vline(3, 0, 6, 1)
logo_inverted.vline(3, 10, 6, 1)

logo_inverted.fill_rect(7, 3, 15, 10, 1)

logo_inverted.vline(14, 0, 16, 1)

logo_inverted.vline(25, 0, 6, 1)
logo_inverted.vline(25, 10, 6, 1)

# Animation: logo slides from top to center

for i in range(9):
    frame.fill(0)
    frame.blit(logo, 18, 0+i)
    
    i2c.writeto(8, frame)
    sleep_ms(200)

# Animation: display color inverts a couple of times

display_inverted = 0
for i in range(6):
    if display_inverted:
        frame.fill(0)
        frame.blit(logo, 18, 8)
        
        display_inverted = 0
     
    else:
        frame.fill(1)
        frame.blit(logo_inverted, 18, 8)
        
        display_inverted = 1
    
    i2c.writeto(8, frame)
    sleep_ms(200)