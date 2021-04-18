# Write your code here :-)

import time
import board
import digitalio
import microcontroller

print(dir(board))

"""CircuitPython Essentials Pin Map Script"""
print('RPi Pico Test')
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

TFT_CS_PIN    = GP17
TFT_DC_PIN    = GP20
TFT_RESET_PIN = GP21

TFT_MOSI_PIN  = GP19
TFT_MISO_PIN  = GP16
TFT_SCK_PIN   = GP18

tft_cs = digitalio.DigitalInOut(TFT_CS_PIN )
tft_cs.direction = digitalio.Direction.OUTPUT
tft_dc = digitalio.DigitalInOut(TFT_DC_PIN )
tft_dc.direction = digitalio.Direction.OUTPUT
tft_reset = digitalio.DigitalInOut(TFT_RESET_PIN )
tft_reset.direction = digitalio.Direction.OUTPUT

print(dir(board))
board_pins = []
for pin in dir(microcontroller.pin):
    if isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin):
        pins = []
        for alias in dir(board):
            if getattr(board, alias) is getattr(microcontroller.pin, pin):
                pins.append("board.{}".format(alias))
        if len(pins) > 0:
            board_pins.append(" ".join(pins))
for pins in sorted(board_pins):
    print(pins)

print(help("modules"))

yellow_button = digitalio.DigitalInOut(board.GP14)
yellow_button.switch_to_input(pull=digitalio.Pull.UP)
red_button = digitalio.DigitalInOut(board.GP15)
red_button.switch_to_input(pull=digitalio.Pull.UP)


while red_button.value:
    print(yellow_button.value)
    time.sleep(0.5)


while True:
    led.value = not led.value
    time.sleep(0.5)