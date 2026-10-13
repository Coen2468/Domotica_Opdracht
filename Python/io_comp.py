_TRUE_CHARACTERS = ("Y", "j", "y", "J")

def invoer(knopnummer: int) -> bool:
    """ We vragen of een drukknop is ingedrukt.
        returns True wanneer ingedrukt, False als deze niet is ingedrukt
    """
    tekst = "Is knop " + str(knopnummer) + " ingedrukt? :  (Y/N): "
    return input(tekst) in (_TRUE_CHARACTERS)

def wcd1(aan: bool) -> None:
    " We zetten hier WCD1 aan "
    print(f"wcd 1  :{aan:5}")

def wcd2(aan: bool) -> None:
    " We zetten hier WCD2 aan "
    print(f"wcd 2  :{aan:5}")

def lamp1(aan: bool) -> None:
    " We zetten hier lamp1 aan "
    print(f"lamp 1 :{aan:5}")

def lamp2(aan: bool) -> None:
    " We zetten hier lamp2 aan "
    print(f"lamp 2 : {aan:5}")

def lamp3(aan: bool) -> None:
    " We zetten hier lamp3 aan "
    print(f"lamp 3 : {aan:5}")

if __name__ == "__main__":
    print( "Hier komen de testen van deze functie:")
    print( f"Antwoord knop 1 : {invoer(1)}")
    print( f"Antwoord knop 2 : {invoer(2)}")
    print( f"Antwoord knop 3 : {invoer(3)}")
    
    wcd1 (True)
    wcd1 (False)
    
    wcd2 (True)
    wcd1 (False)
    
    lamp1 (True)
    lamp1 (False)
    
    lamp2 (True)
    lamp2 (False)
    
    lamp3 (True)
    lamp3 (False)
