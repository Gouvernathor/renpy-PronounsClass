# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
define e = Person(Character("Eileen"), gender=FEMALEGENDER)
define angrye = Person(Character("Eileen"), gender=FEMALEGENDER, pronouns=["HE", "HIM", "HIS"]) # it's not mandatory to fill all the pronouns
define remy = Person(Character("Remy")) # gender defaults to neutral
define jamie = Person(Character("Jamie"), gender="Nonebinariii") # setting a custom gender is treated as neutral by default
define doug = Person(Character("Douglas Stamper"), gender=MALEGENDER, name="Doug")


# The game starts here.

label start:
    # These display lines of dialogue.

    e.char "You've created a new Ren'Py game."
    
    "Oh no ! All characters here seem to adress themselves in the third person !"
    e.char "Hi ! [e.theyare!c] named [e.name], and adressing [e.them]self at the third person is so cool ! My gender is [e.gender]."
    angrye.char "Hi ! [angrye.theyare!c] named [angrye.name], and adressing [angrye.them]self at the third person is so cool ! My gender is [angrye.gender]."
    remy.char "Hi ! [remy.theyare!c] named [remy.name], and adressing [remy.them]self at the third person is so cool ! My gender is [remy.gender]."
    doug.char "Hi ! [doug.theyare!c] named [doug.name], and adressing [doug.them]self at the third person is so cool ! My gender is [doug.gender]."
    
    # unfortunately something like ("They adress/He adresses") can't be treated properly
    # as it would either need one property per verb, since methods or functions can't be called in dialogue substitution.

    # This ends the game.

    return
