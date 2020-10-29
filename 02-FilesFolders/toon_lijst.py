import os

huidige_map = os.getcwd()
alle_bestanden = os.scandir(huidige_map)
print("Inhoudsopgave van de map: " + huidige_map)
for bestand in alle_bestanden:
    if bestand.is_file():
        print(bestand.name + " (bestand)")
    elif bestand.is_dir():
        print(bestand.name + " (map)")
    else:
        print(bestand.name + " (onbekend type")
