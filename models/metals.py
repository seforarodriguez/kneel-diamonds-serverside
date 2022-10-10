class Metal():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, price):
        self.id = id
        self.metal = name
        self.price = price

new_metal = Metal(1, "Sterling Silver", 12.42)