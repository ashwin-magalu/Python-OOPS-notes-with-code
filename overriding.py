class India:
    def language(self):
        print("There are 23 Official languages in India")


class Karnataka(India):
    def language(self):
        print("Kannada")

class UP(India):
    def language(self):
        super().language()

ind = India()
ind.language()
kar = Karnataka()
kar.language()
up = UP()
up.language()