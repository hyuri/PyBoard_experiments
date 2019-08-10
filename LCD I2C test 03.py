# Auto-centering text
# Single-pixel animations

import machine
from framebuf import FrameBuffer, MONO_HLSB, RGB565
from time import sleep_ms

scl = machine.Pin('X9')
sda = machine.Pin('X10')
i2c = machine.I2C(scl=scl, sda=sda)

frame_size = [64, 32]

text = "Test" # Up to 8 characters in a 64px wide screen
text_hsize = len(text) * 8
centered_text_start = [int((frame_size[0] / 2) - (text_hsize / 2)), int((frame_size[1] / 2) - (8 / 2))]

# Frame buffers
main_frame = FrameBuffer(bytearray(frame_size[0] * frame_size[1] // 8), frame_size[0], frame_size[1], MONO_HLSB)
text_frame = FrameBuffer(bytearray(text_hsize * 8 // 8), text_hsize, 8, MONO_HLSB)
pixel_frame = FrameBuffer(bytearray(1), 1, 1, MONO_HLSB)
pixel_frame_black = FrameBuffer(bytearray(1), 1, 1, MONO_HLSB)

# Text
text_frame.fill(0)
text_frame.text(text, 0, 0, 1)

# Single-Pixels
pixel_frame.fill(0)
pixel_frame.pixel(0, 0, 1)

pixel_frame_black.pixel(0, 0, 0)

# Drawing text_frame on top of main_frame
main_frame.fill(0)
main_frame.blit(text_frame, centered_text_start[0], centered_text_start[1])

# Animation: underline
for i in range(text_hsize):
    main_frame.blit(pixel_frame, centered_text_start[0] + i, centered_text_start[1] + 9)

    i2c.writeto(8, main_frame)

# Animation: blinking period
period_visible = 0
for i in range(5):
    if period_visible:
        main_frame.blit(pixel_frame_black, centered_text_start[0] + text_hsize + 1, centered_text_start[1] + 9)
        
        period_visible = 0
    
    else:
        main_frame.blit(pixel_frame, centered_text_start[0] + text_hsize + 1, centered_text_start[1] + 9)
        
        period_visible = 1

    i2c.writeto(8, main_frame)