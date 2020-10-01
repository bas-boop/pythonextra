import os

werkmap = os.getcwd()
print("De huidige map is: " + werkmap)
os.mkdir("Een nieuwe map")

#mapnaam = input("Welke naam wil je voor de map?")

#lengte_mapnaam = len(mapnaam)
#if lengte_mapnaam > 0:
   # os.mkdir(mapnaam)
  #  print("De map " + mapnaam + " is gemaakt.")
#else:
  #  print("Je hebt geen naam ingevoerd!")

mapnaam = ""
lengte_mapnaam = 0
while lengte_mapnaam == 0:

    mapnaam = input("welke naam wil je voor deze map?")
    lengte_mapnaam = len(mapnaam)

    if lengte_mapnaam > 0:
        os.mkdir(mapnaam)
    else:
        print("REEEEEEEEEEEEEEEEEEEEEEEEEEEEE waarom geef je een map geen naam!")
print("De map " + mapnaam + " is gemaakt.")

bestand = open("test.txt", "w")
bestand.write("Test 1 2 3 !");
bestand.close()

import io

bestand2 = open("test.txt", "r")
bestand2.write("Lekker alles overschrijven")
