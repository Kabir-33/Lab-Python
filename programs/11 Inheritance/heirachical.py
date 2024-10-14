class car:
    def company(self):
        print("The company is Mahindra...")

class Bolero(car):
    def model(self,name,model,mileage):
        name=self.name
        model=self.model
        mileage=self.mileage

    def info(self,name,model,mileage):
        print("The car is ",name)
        print("Model is ",model)
        print("Mileage is ",mileage)

class Thar(car):
    def model(self):
        print("The car is Thar")
        print("Model is 2022...")
        print("Mileage is 16...")


b=Bolero()
b.info("Bolero B6",2023,25)

print("------------------------------------------")

t=Thar()
t.model()