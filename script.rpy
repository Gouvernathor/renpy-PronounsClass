# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
define e = Person(Character("Eileen"), gender=FEMALEGENDER)
if lang == "en":
    define angrye = Person(Character("Eileen"), gender=FEMALEGENDER, pronouns=["SHE", "HER", "HER"]) # it's not mandatory to fill all the pronouns
elif lang == "fr":
    define angrye = Person(Character("Eileen"), gender=FEMALEGENDER, pronouns=["ELLE", "ELLE", "SA"]) # it's not mandatory to fill all the pronouns
define remy = Person(Character("Remy")) # gender defaults to neutral
define jamie = Person(Character("Jamie"), gender="Nonebinariii") # setting a custom gender is treated as neutral by default
define doug = Person(Character("Douglas Stamper"), gender=MALEGENDER, name="Doug")

# We define the default language of the game
default lang = _preferences.language

# The game starts here.

label start:
    # These display lines of dialogue.

    menu:
        "Choose between these two languages"
        "French":
            $ _preferences.language = "french"
            $ lang = "fr"
        "English":
            $ _preferences.language = None
            $ lang = "en"

    $ e.presents() #E presents herself
    $ angrye.presents() #E Angry presents herself
    $ remy.presents() #Remy presents themself
    $ doug.presents() #Doug presents himself

    menu:
        "start again":
            jump start
        "Quit":
            return
    # unfortunately something like ("They adress/He adresses") can't be treated properly
    # as it would either need one property per verb, since methods or functions can't be called in dialogue substitution.

    # This ends the game.

    return
