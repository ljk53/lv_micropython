import gc
import lvgl as lv
import lvesp32

from machine import Pin, SPI, I2S, SPI, mpu6886, axp192, bm8563, ft6336u
from axpili9342 import ili9342
from m5stack import M5Stack

m5core = M5Stack()

display = ili9342(m5stack=m5core)
mpu = mpu6886()
clock = bm8563()
touch = ft6336u()

scr = lv.obj()
btn = lv.btn(scr)
btn.align(lv.scr_act(), lv.ALIGN.CENTER, 0, 0)
label = lv.label(btn)
label.set_text("Button")

# Load the screen
lv.scr_load(scr)
