#!/usr/bin/python
import spidev
import time
DEBUG = 0

spi = spidev.SpiDev()
spi.open(0,0)

# read SPI data from MCP3202 chip
def get_adc(channel):
    # Only 2 channels 0 and 1 else return -1
    if ((channel > 1) or (channel < 0)):
        return -1
    r = spi.xfer2([1,(2+channel)<<6,0])
    
    ret = (((r[1]&0x0F) << 8) + (r[2]))
    return ret


tempval = 0
promval = 0
promval_8b = 0
for x in range(0, 9):
    tempval += get_adc(0)
    promval = tempval/10.0
    promval_8b = promval*(256/4096.0)
    print "Valor Decimal 12 bits: %0.5f" % promval
    print "Valor Decimal: 8 bits %0.5f"   %promval_8b

