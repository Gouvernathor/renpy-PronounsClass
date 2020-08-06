# RenPron-class
A Person class for Ren'py able to manage the pronouns of one or several characters.

The `personclass.rpy` file contains the python class itself (and the constants that goes with it).

The `script.rpy` file contains some example as to how to use it in dialogue. More specifically, it is showing :
- how to create `Person`s (not the birds and the bees)
- how to use the `.char` as talking characters
- how to set and access custom names, different from the `.char` name
- how to set and access genders
- how to set and use custom pronouns (warning though, using an incomplete set of pronouns for a neutral-managed character causes glitches for the `.theyre` and `.theyare` forms)
- how to manage capitalization of interpolated text (it's a basic renpy functionality, but the file shows it nonetheless)

A `tl` folder may be added later for an example of how to translate it to other languages.
