# TFT_ILI9341
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.

Pinouts are for the 2.8" TFT Shield
"""
import time
import board
import busio
import terminalio
import displayio
import digitalio
import microcontroller
from adafruit_display_text import label
import adafruit_ili9341

TFT_CS_PIN    = board.GP22
TFT_DC_PIN    = board.GP20
TFT_RESET_PIN = board.GP21

TFT_MOSI_PIN  = board.GP19
TFT_MISO_PIN  = board.GP16
TFT_SCK_PIN   = board.GP18


# tft_cs = TFT_CS_PIN
# tft_dc = TFT_DC_PIN
'''
tft_cs = digitalio.DigitalInOut(TFT_CS_PIN )
tft_cs.direction = digitalio.Direction.OUTPUT
tft_dc = digitalio.DigitalInOut(TFT_DC_PIN )
tft_dc.direction = digitalio.Direction.OUTPUT
tft_reset = digitalio.DigitalInOut(TFT_RESET_PIN )
tft_reset.direction = digitalio.Direction.OUTPUT
'''
# tft_mosi = digitalio.DigitalInOut(TFT_MOSI_PIN )
# tft_mosi.direction = digitalio.Direction.OUTPUT
# tft_miso = digitalio.DigitalInOut(TFT_MISO_PIN )
# tft_miso.direction = digitalio.Direction.OUTPUT

# tft_sck = digitalio.DigitalInOut(TFT_SCK_PIN )
# tft_sck.direction = digitalio.Direction.OUTPUT


# tft_reset.value = 1
# time.sleep(1.00)
# tft_reset.value = 0
# time.sleep(1.00)
# tft_reset.value = 1

# tft_miso.value = 1
# time.sleep(2.00)
# tft_miso.value = 0
# while True:
#     pass


# Release any resources currently in use for the displays
displayio.release_displays()

# Use Hardware SPI
# spi = board.SPI()

# Use Software SPI if you have a shield with pins 11-13 jumpered
# import busio
# spi = busio.SPI(board.D11, board.D13)
spi_tft = busio.SPI(clock=TFT_SCK_PIN, MOSI=TFT_MOSI_PIN, MISO=TFT_MISO_PIN)

display_bus = displayio.FourWire(spi_tft, command=TFT_DC_PIN, chip_select=TFT_CS_PIN, reset = TFT_RESET_PIN)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

# Draw a green background
color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(280, 200, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088  # Purple
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)
splash.append(inner_sprite)

# Draw a label
text_group = displayio.Group(max_size=10, scale=3, x=30, y=40)
text = "Raspberry Pi \nPico\nTFT ILI9341\n320x240"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area)  # Subgroup for text scaling

splash.append(text_group)

while True:
    pass