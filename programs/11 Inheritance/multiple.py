class brand:
    def Company(self):
        print("Brand name is Mahindra...")

class model:
    def mod(self):
        print("The Model is Thar...")

class wheeler(brand,model):
    def wheel(self):
        print('You selected the Four Wheeler Segement...')

object=wheeler()
object.wheel()
object.Company()
object.mod()
