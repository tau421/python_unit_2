from abc import ABC, abstractmethod
from pprint import pprint
import csv

class Cupcake(ABC):
    
    def __init__(self, name, flavor, price, filling, frosting, gluten_free):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.filling = filling
        self.frosting = frosting
        self.sprinkles = []
        self.gluten_free = gluten_free

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price

class Regular(Cupcake):
    size = "regular"

    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, flavor, price, frosting, gluten_free):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.frosting = frosting
        self.gluten_free = gluten_free
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price

class Jumbo(Cupcake):
    size = "jumbo"

    def calculate_price(self, quantity):
        return quantity * self.price

mini_cupcake1 = Mini('Small Fry', 'chocolate potato chip', 2, 'chocolate', False)
mini_cupcake1.add_sprinkles(True)
cupcake1 = Regular('Little Tart', 'raspberry lemon', 3, False, 'vanilla', False)
cupcake1.add_sprinkles(False)

cupcake_list = [
    mini_cupcake1,
    cupcake1
]

def read_csv(file):
    with open (file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

def write_new_csv(file, cupcakes):
    with open (file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})   

write_new_csv("sample.csv", cupcake_list)

def append_csv(file, cupcake):
    with open (file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})