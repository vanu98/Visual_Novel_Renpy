# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character('Ayumi', color="#c8ffc8")
define v = Character('Albus', color="#c8c8ff")

image Ayumi = "images/c2.png"
image Albus happy = "images/c1.png"
image school = "images/bbg.jpg"
# The game starts here.

label start:

    show school
    with fade

    "After a long summer break, Albus wants o express his feelings to Ayumi"

    "It's a beautiful morning. Albu see's Ayumi near th lobby."

    show Albus happy at left
    with dissolve
    v "Hey... Umm..."


    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"
    show  Ayumi at right
    v "Ummm... Will you..."

    v "Would you like to go out for a coffee with me?"
    "She Blushess...."
    a "hmmm.. ya sure!!"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
