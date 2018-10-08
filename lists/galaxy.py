import time
import sys

def load_ship():
    print("Lists are powerful data structures that can grow and shrink depending on the developer's needs...")
    print("Let's use a list to explore the planets in our galaxy!")
    print()

# MOON DATA
mercury = []
venus = []
earth = ["Moon"]
mars = ["Deimos", "Phobos"]
jupiter = ["Metis", "Adrastea", "Amalthea", "Thebe", "Io", "Europa", "Ganymede", "Callisto", "Themisto", "Leda", "Himalia", "Lysithea", "Elara", "S/2000 J 11", "Carpo", "S/2003 J 12", "Euporie", "S/2003 J 3", "S/2003 J 18 ",
"S/2011 J 1", "S/2010 J 2", "Thelxinoe", "Euanthe", "Helike", "Orthosie", "Iocaste", "S/2003 J 16", "Praxidike", "Harpalyke", "Mneme", "Hermippe", "Thyone", "Ananke", "Herse", "Aitne", "Kale", "Taygete", "S/2003 J 19", "Chaldene"
, "S/2003 J 15", "S/2003 J 10", "S/2003 J 23", "Erinome", "Aoede", "Kallichore", "Kalyke", "Carme", "Callirrhoe", "Eurydome", "S/2011 J 2", "Pasithee", "S/2010 J 1", "Kore", "Cyllene", "Eukelade", "S/2003 J 4", "Pasipha", "Hegemone"
, "Arche", "Isonoe", "S/2003 J 9", "S/2003 J 5", "Sinope", "Sponde", "Autonoe", "Megaclite", "S/2003 J 2"]
saturn = ["Pan", "Daphnis", "Atlas", "Prometheus", "Pandora", "Epimetheus", "Janus", "Aegaeon", "Mimas", "Methone", "Anthe", "Pallene", "Enceladus", "Tethys", "Telesto", "Calypso", "Dione", "Helene", "Polydeuces", "Rhea", "Titan", "Hyperion", "Iapetus", "Kiviuq", "Ijiraq", "Phoebe", "Paaliaq", "Skathi", "Albiorix", "S/2007 S 2", "Bebhionn", "Erriapo", "Skoll", "Siarnaq", "Tarqeq", "S/2004 S 13", "Greip", "Hyrrokkin", "Jarnsaxa", "Tarvos", "Mundilfari", "S/2006 S 1", "S/2004 S 17", "Bergelmir", "Narvi", "Suttungr", "Hati", "S/2004 S 12", "Farbauti", "Thrymr", "Aegir", "S/2007 S 3", "Bestla", "S/2004 S 7", "S/2006 S 3", "Fenrir", "Surtur", "Kari", "Ymir", "Loge", "Fornjot"]
uranus = [ "Ariel", "Belinda", "Bianca", "Caliban", "Cordelia", "Cressida", "Cupid", "Desdemona", "Ferdinand", "Francisco", "Juliet", "Mab", "Margaret", "Miranda", "Oberon", "Ophelia", "Perdita", "Portia", "Prospero", "Puck", "Rosalind", "Setebos", "Stephano", "Sycorax", "Titania", "Trinculo", "Umbriel" ]
neptune = ["Triton", "Proteus", "Nereid", "Larissa", "galatea", "Despina", "Thalassa", "Naiad", "Halimede", "Neso", "Sao", "Laomedeia", "Psamathe", "S/2004 N1"]
pluto = ["Charon", "Hydra", "Kerberos", "Nix", "Styx"]

def prompt(moon_count):
    print("You have explored " + str(moon_count) + " moons!")
    print("""
    1 - Mercury
    2 - Venus
    3 - Earth
    4 - Mars
    5 - Jupiter
    6 - Saturn
    7 - Uranus
    8 - Neptune
    9 - Pluto
    """)
    choice = input("Enter a number to find out which moons orbit that planet or 0 to exit.\nPLANET CHOICE: ")
    
    if choice == "0":
        print("Thank you for exploring the solar system with Codecademy!")
        exit()
    else:
        if choice == "1":
            print("Mercury is one of the few planets with no moons! :-()")
            prompt(moon_count)
        if choice == "2":
            print("Venus is one of the few planets with no moons! :-()")
            prompt(moon_count)
        if choice == "3":
            for x in earth:
                moon_count += 1
                print(str(moon_count) + ". " + x)
            prompt(moon_count)
        if choice == "4":
            for x in mars:
                moon_count += 1
                print(str(moon_count) + ". " + x)
            prompt(moon_count)
        if choice == "5":
            for x in jupiter:
                moon_count += 1
                print(str(moon_count) + ". " + x)
            prompt(moon_count)
        if choice == "6":
            for x in saturn:
                moon_count += 1
                print(str(moon_count) + ". " + x)
            prompt(moon_count)
        if choice == "7":
            for x in uranus:
                moon_count += 1
                print(str(moon_count) + ". " + x)
            prompt(moon_count)
        if choice == "8":
            for x in neptune:
                moon_count += 1
                print(str(moon_count) + ". " + x)
            prompt(moon_count)
        if choice == "9":
            for x in pluto:
                moon_count += 1
                print(str(moon_count) + ". " + x)
            prompt(moon_count)
        print("Please pick a number between 0 and 9")
        prompt(moon_count)
