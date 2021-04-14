import time
import board
import digitalio
import microcontroller
import busio
import adafruit_msa301
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
# import adafruit_ssd1306

displayio.release_displays()

WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 1

i2c = busio.I2C(scl=board.GP3, sda=board.GP2)
# oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT,i2c,addr=0x3c)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)


yellow_button = digitalio.DigitalInOut(board.GP14)
yellow_button.switch_to_input(pull=digitalio.Pull.UP)
red_button = digitalio.DigitalInOut(board.GP15)
red_button.switch_to_input(pull=digitalio.Pull.UP)

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(
    terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT // 4 - 1
)
splash.append(text_area)
text = "Row 2"
text_area2 = label.Label(
    terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT -10)
splash.append(text_area2)

while True:
    pass


#oled.fill(1)
#oled.show()

msa = adafruit_msa301.MSA301(i2c)
while red_button.value:
    print(msa.acceleration)
    time.sleep(0.05)