#multiple inheritance
class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

# Usage
duck = Duck()
print(duck.fly())   # Output: Flying
print(duck.swim())  # Output: Swimming
print(duck.quack()) # Output: Quack!
