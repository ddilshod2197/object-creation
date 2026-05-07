class Object:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"Object: {self.name}, Color: {self.color}, Weight: {self.weight} kg"

# Object yaratish
object1 = Object("Kamera", "Qora", 0.5)
print(object1)
