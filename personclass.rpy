define MALEGENDER = _("Male")
define FEMALEGENDER = _("Female")
# you could set these as man/woman, doesn't really matter
define MALEGENDERS = {MALEGENDER}
define FEMALEGENDERS = {FEMALEGENDER}
# You can add more male- or female-managed genders in these sets.



init python:

    class Person(object):
        if _preferences.language == None:
            lang = "en" #We define a new variable we'll use in this class, here we are in english
        if _preferences.language == "french":
            lang = "fr" #We define a new variable we'll use in this class, here we are in french
        """To manipulate gender, pronouns, customizable infos, Characters, and maybe layeredimages from a single place !"""
        def __init__(self, char=adv, gender=None, pronouns=[], name=None, disp=None):
            super(Person, self).__init__()
            self.char = char # an instance of Character() goes here (or the empty nameless character by default)
            self.gender = gender # MALEGENDER, FEMALEGENDER, or some custom stuff
            self.__they, self.__them, self.__their, self.__theyre, self.__theyare = (pronouns+[None]*5)[:5] # [they, them, their, they're, they are] as strings
            self.__name = name or self.char.name # useful if not setting a char, or if using different names between dialog labels and anywhere else
            self.disp = disp # a Displayable or a list thereof, doesn't really mater as it's meant to be accessed directly in the code
            self.__undefined = " a" #I don't know how to explain it...

        @property
        def name(self):
            return self.__name or self.char.name
        @name.setter
        def name(self, name):
            self.__name = name

        ## The pronouns
        # The capitalized versions of the pronouns ("They" for "they", etc) are not included
        # to prevent code duplication
        # and because "[remy.them!cl]" does the same as "[remy.Them]" would.
        # The *self version has been also omitted because you can use "[remy.them]self"
        # However, you can add these attributes yourself if you want to
        # You can also override this way of figuring the pronouns for a specific set of characters
        # by subclassing the Person class and overriding these property methods

        def __pronounchoice(self, masc, fem, neut):
            """Makes the actual choice between pronoun options"""
            if self.gender in MALEGENDERS:
                return masc
            elif self.gender in FEMALEGENDERS:
                return fem
            else:
                return neut

        @property
        def they(self):
            if lang == "en":
                return self.__they or self.__pronounchoice(_("he"), _("she"), _("they"))
            elif lang == "fr":
                return self.__they or self.__pronounchoice(_("il"), _("elle"), _("ils"))
            # apply any changes to these constants also in the theyre() method !
        @they.setter
        def they(self, they):
            self.__they = they

        @property
        def them(self):
            if lang == "en":
                return self.__them or self.__pronounchoice(_("him"), _("her"), _("them"))
            elif lang == "fr":
                return self.__them or self.__pronounchoice(_("lui"), _("elle"), _("eux"))
        @them.setter
        def them(self, them):
            self.__them = them

        @property
        def their(self):
            if lang == "en":
                return self.__their or self.__pronounchoice(_("his"), _("her"), _("their"))
            elif lang == "fr":
                return self.__their or self.__pronounchoice(_("son"), _("sa"), _("leur"))
        @their.setter
        def their(self, their):
            self.__their = their

        def __pluralchoice(self, sing, plur):
            th = self.they
            if lang == "en":
                if th in {_("they")}: # could have used == but this way is simpler to add plural pronouns
                    return th+plur
                elif th in {_("he"), _("she")} or self.gender in MALEGENDERS|FEMALEGENDERS:
                    return th+sing
                else:
                    # will only happen if self.they() returns something unexpected
                    # for example if you modify the pronoun constants in self.they() and forget to apply them here
                    # or if the character has another pronoun and no binary gender
                    raise NotImplementedError
                    # raises an exception if used in python code, but not in dialogue
                    # where it will display the [remy.theyre] clause verbatim
            elif lang == "fr":
                if th in {_("ils")}: # could have used == but this way is simpler to add plural pronouns
                    return th+plur
                elif th in {_("il"), _("elle")} or self.gender in MALEGENDERS|FEMALEGENDERS:
                    return th+sing
                else:
                    raise NotImplementedError


        @property
        def theyre(self):
            return self.__theyre or self.__pluralchoice(_("'s"), _("'re"))
        @theyre.setter
        def theyre(self, theyre):
            self.__theyre = theyre

        @property
        def theyare(self):
            if lang == "en":
                return self.__theyare or self.__pluralchoice(_(" is"), _(" are"))
            elif lang == "fr":
                return self.__theyare or self.__pluralchoice(_(" est"), _(" sont"))
        @theyare.setter
        def theyare(self, theyare):
            self.__theyare = theyare

        @property
        def undefined(self):
            if lang == "en":
                return self.__undefined
            elif lang == "fr":
                return self.__pronounchoice(_(" un"), _(" une"), _(" un"))

        ###Actions
        def presents(self): # This function lets you writing less lines of code
            if self.gender in MALEGENDERS:
                prono = "de "
            elif self.gender in FEMALEGENDERS:
                prono = "d'"
            else:
                prono = "de "
            if lang == "en":
                renpy.say(self.char, "Hi! "+str(self.theyare)+" named "+str(self.name)+", and adressing "+str(self.them)+"self at the third person is so cool! It's"+str(self.undefined)+" "+str(self.gender)+".")
            elif lang == "fr":
                renpy.say(self.char, "Hé ! "+str(self.theyare)+" "+str(self.name)+", et parle "+prono+str(self.them)+" à la troisième personne, c'est tellement cool ! C'est"+str(self.undefined)+" "+str(self.gender)+".")
            else:
                renpy.say("", "Sorry but it's not working")
