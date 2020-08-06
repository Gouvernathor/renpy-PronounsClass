define MALEGENDER = _("Male")
define FEMALEGENDER = _("Female")

init python:

    class Person(object):
        """To manipulate gender, pronouns, customizable infos, Characters, and maybe layeredimages from a single place !"""
        def __init__(self, char=adv, gender=None, pronouns=[None, None, None, None, None], name=None, disp=None):
            super(Person, self).__init__()
            self.char = char # an instance of Character() goes here (or the empty nameless character by default)
            self.gender = gender # MALEGENDER, FEMALEGENDER, or some custom stuff
            self.__they, self.__them, self.__their, self.__theyre, self.__theyare = pronouns # [they, them, their, they're, they are] as strings
            self.__name = name or self.char.name # useful if not setting a char, or if using different names between dialog labels and anywhere else
            self.disp = disp # a Displayable or a list thereof, doesn't really mater as it's meant to be accessed directly in the code

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
            if self.gender == MALEGENDER:
                return masc
            elif self.gender == FEMALEGENDER:
                return fem
            else:
                return neut

        @property
        def they(self):
            return self.__they or self.__pronounchoice(_("he"), _("she"), _("they"))
            # apply any changes to these constants also in the theyre() method !
        @they.setter
        def they(self, they):
            self.__they = they

        @property
        def them(self):
            return self.__them or self.__pronounchoice(_("him"), _("her"), _("them"))
        @them.setter
        def them(self, them):
            self.__them = them

        @property
        def their(self):
            return self.__their or self.__pronounchoice(_("his"), _("her"), _("their"))
        @their.setter
        def their(self, their):
            self.__their = their

        def __pluralchoice(self, sing, plur):
            th = self.they
            if th in {_("they")}: # could have used == but this way is simpler to add plural pronouns
                return th+plur
            elif th in {_("he"), _("she")} or self.gender in {MALEGENDER, FEMALEGENDER}:
                return th+sing
            else:
                # will only happen if self.they() returns something unexpected
                # for example if you modify the pronoun constants in self.they() and forget to apply them here
                # or if the character has another pronoun and no binary gender
                raise NotImplementedError

        @property
        def theyre(self):
            return self.__theyre or self.__pluralchoice(_("'s"), _("'re"))
        @theyre.setter
        def theyre(self, theyre):
            self.__theyre = theyre

        @property
        def theyare(self):
            return self.__theyare or self.__pluralchoice(_(" is"), _(" are"))
        @theyare.setter
        def theyare(self, theyare):
            self.__theyare = theyare
