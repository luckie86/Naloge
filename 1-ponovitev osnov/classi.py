
class Lastnik ():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


class Avto ():
    def __init__(self, model, year):
        self.model = model
        self.year = year


bmw = Avto(model="x5", year="1986")
luka = Lastnik(name="Luka", lastname="Brinar")

print bmw.model
print luka.name