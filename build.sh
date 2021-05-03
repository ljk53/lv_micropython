#!/bin/sh

export BOARD=M5CORE2_BOARD
make -C mpy-cross
make -C ports/esp32 LV_CFLAGS="-DLV_COLOR_DEPTH=16 -DLV_COLOR_16_SWAP=1" PYTHON=python3 MICROPY_PY_BTREE=0

echo "Flash: esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 ports/esp32/build-M5CORE2_BOARD/firmware.bin"
