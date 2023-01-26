class Cupcake:
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

cupcake1 = Cupcake('Little Tart', 'raspberry lemon', 3, False, 'vanilla', False)

cupcake1.add_sprinkles(False)

print(cupcake1.sprinkles)