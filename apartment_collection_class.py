class House:
    def __init__(self, street, town, price):
        self.street = street
        self.town = town
        self.price = price

    def __repr__(self):
        return f"The home is located on {self.street} in {self.town} at a price of ${self.price}"
    
class Condo (House):
    def __init__(self, street, town, price, neighborhood):
        super().__init__(street, town, price)
        self.neighborhood = neighborhood

    def __repr__(self):
        return f"The home is located on {self.street} in {self.town} at a price of ${self.price} in the {self.neighborhood} neighborhood"
    
colonial = House('12 Main Street', 'Brookline', 550000)
loft = Condo('34 Center Street', 'Boston', 400000, 'Back Bay')

print(colonial)
print(loft)

#optional:  add len, getitem, for loop, and @classmethod