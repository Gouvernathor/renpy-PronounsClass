# The script of the game goes in this file.

# Declare characters used by this game.
# Character objects are meant to be defined, as always
# Person objects are meant to be defaulted, because they can change during playthrough

define character.e = Character("Eileen")
default e = pron.Person(gender=FEMALEGENDER)
default angrye = pron.Person(gender=FEMALEGENDER, pronouns=["HE", "HIM", "HIS"]) # it's not mandatory to fill all the pronouns
define character.remy = Character("Remy")
default remy = pron.Person() # gender defaults to neutral
define character.jamie = Character("Jamie")
default jamie = pron.Person(gender="Nonebinariii") # setting a custom gender is treated as neutral by default
define character.doug = Character("Douglas Stamper")
default doug = pron.Person(gender=MALEGENDER, name="Doug")


# The game starts here.

label start:
    menu:
        "What gender should Eileen use ?"
        "Male":
            $ e.gender = pron.MALEGENDER
        "Female":
            $ e.gender = pron.FEMALEGENDER
        "Neutral":
            $ e.gender = None

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    # The speaker will be looked for in the character.x pool in priority, accessing the Character objects.
    # The square-bracket interpolation will not, and will only access the Person objects.

    "Oh no ! All characters here seem to adress themselves in the third person !"
    e "Hi ! [e.theyare!c] named [character.e], and adressing [e.them]self at the third person is so cool ! My gender is [e.gender!l]."
    angrye "Hi ! [angrye.theyare!c] named [character.angrye], and adressing [angrye.them]self at the third person is so cool ! My gender is [angrye.gender!l]."
    remy "Hi ! [remy.theyare!c] named [character.remy], and adressing [remy.them]self at the third person is so cool ! My gender is [remy.gender!l]."
    jamie "Hi ! [jamie.theyare!c] named [character.jamie], and adressing [jamie.them]self at the third person is so cool ! My gender is [jamie.gender!l]."
    doug "Hi ! [doug.theyare!c] named [doug.name], and adressing [doug.them]self at the third person is so cool ! My gender is [doug.gender!l]."

    # unfortunately something like ("They adress/He adresses") can't be treated properly
    # as it would need one property per verb, since methods or functions can't be called in dialogue substitution.

    # This ends the game.

    return
