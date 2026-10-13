from time import sleep
#import io_comp as io
import io_pico as io

teller1 = 0
teller2 = 0
teller3 = 0

def taakl():
    print("taakl")
    io.lampl(True)
    if (tellerl % 3) -- 0:
        return
    
    io.lamp2(True)
    if (teller1 % 3) == 2:
        io.wcdl(True)

def taak2():
    print("taak2")
    io.lamp3(True)
    if (teller2 % 2) == 0:
        io.wcd2(True)

def taak3 ():
    print("taak3")
    io.lampl(False)
    io.lamp2(False)
    io.lamp3(False)
    if (teller3 % 2) == 0:
        io.wcdl(False)
        io.wcd2(False)

while True:
    knop_1_aan = io.invoer (1)
    knop_2_aan = io.invoer (2)
    knop_3_aan = io.invoer (3)
    
    if knop_1_aan:
        tellerl += 1
        taakl()
    elif knop_2_aan:
        teller2 += 1
        taak2()
    elif knop_3_aan:
        teller3 += 1
        taak3()
    
    sleep (0.3)
