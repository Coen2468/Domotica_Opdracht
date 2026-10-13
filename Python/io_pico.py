from machine import Pin
from time import sleep

sleep(2)

_drukknop1 = Pin(8, Pin.IN)
_drukknop2 = Pin(7, Pin.IN)
_drukknop3 = Pin(6, Pin.IN)

_relais_01 = Pin(28, Pin.OUT)
_relais_02 = Pin(27, Pin.OUT)
_relais_03 = Pin(26, Pin.OUT)
_relais_04 = Pin(21, Pin.OUT)
_relais_05 = Pin(17, Pin.OUT)


def invoer(knopnummer: int) -> bool:
    """We vragen of een drukknop is ingedrukt. returns True wanneer ingedrukt, False als deze niet is ingedrukt
    """
    if knopnummer == 1:
        return _drukknop1.value() == 1
    if knopnummer == 2:
        return _drukknop2.value() == 1
    if knopnummer == 3:
        return _drukknop3.value() == 1
    return False


def wcd1(aan: bool) -> None:
    " We zetten hier WCD1 aan "
    if aan:
        _relais_01.on()
    else:
        _relais_01.off()


def wcd2(aan: bool) -> None:
    " We zetten hier WCD2 aan "
    if aan:
        _relais_02.on()
    else:
        _relais_02.off()


def lamp1(aan: bool) -> None:
    " We zetten hier lamp1 aan "
    if aan:
        _relais_03.on()
    else:
        _relais_03.off()


def lamp2(aan: bool) -> None:
    " We zetten hier lamp2 aan "
    if aan:
        _relais_04.on()
    else:
        _relais_04.off()


def lamp3(aan: bool) -> None:
    " We zetten hier lamp3 aan "
    if aan:
        _relais_05.on()
    else:
        _relais_05.off()

def test_buttons():
    " Hier komen de testen van deze functie "
    teller = 0
    while True:
        print(10 * "-", teller, 10 * "-")
        print("Status knop 1 = ", invoer(1))
        print("Status knop 2 = ", invoer(2))
        print("Status knop 3 = ", invoer(3))

        wcd1(teller % 2 == 0)
        wcd2(teller % 2 == 0)
        lamp1(teller % 2 == 0)
        lamp2(teller % 2 == 0)
        lamp3(teller % 2 == 0)

        sleep(1)
        teller += 1