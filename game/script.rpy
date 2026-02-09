# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define b = Character("Beolco")  # the goat, student at parnassus
define ts = Character("The Scop") # founder of parnassus
define tsw = Character("The Silent Whisper") #appears in part 1: the companions. beolco's parents appear too, but they dont need their own tag
define c = Character("Chanticleer") # the cat im 99.99999% sure, clown college, in band
define d = Character("Devereaux") # the gator, student at clown college
define dg = Character("Devereaux's Grandfather") #will probably be needed
define m = Character("Malory") # the bird, member of birds of paradise. not sure what school yet
define lg = Character("Lady Gay") #bird mother
define t = Character("Tiberius") # in the band, clown college, other gator
define a = Character("Artemis") # in the band, clown college, purple cat im pretty sure
# potentially add the birds of doubt, distraction, and drowsiness
define p = Character("Perimones") # parnassus? suspect of stealing the skull of the college bard. Potentially this dino guy? Proably not?
# part 2: the ransom
define r = Character("Rosa") # kangaroo? med student at parnassus w/ healing powers
define beh = Character("Behemoth") # ancient being rosa uncovers and seems to b haunted by?
define h = Character("Hyacinth") # dean of parnassus lib arts, poisoned
define l = Character("Leander") # not sure yet
define ta = Character("The Accuser") # not sure yet


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    c "Chanticleer"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
