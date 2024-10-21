class India:
    def capital(self):
        print("Capital is New Delhi..")
    def language(self):
        print("Hindi is most Comman Language...")
    def type(self):
        print("India is Developing Country...")
        print()

class USA:
    def capital(self):
        print("Capital is Washington DC")
    def language(self):
        print("English is most commonly used...")
    def type(self):
        print("USA is developed nation..")
        print()

ind=India()
usa=USA()
for country in (ind,usa):
    country.language()
    country.capital()
    country.type()