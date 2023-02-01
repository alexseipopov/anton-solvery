class Writting_items:
    def __init__(self, length, color, mechanism):
        self.length = length
        self.color = color
        self.mechanism = mechanism
    
    def __repr__(self):
        return f"Im a pan. i have {self.length} len. my color is {self.color}. My mechanism is {self.mechanism}"

class Pencil(Writting_items):
    def write(self):
        print(f"im PANCIL -  writting {self.color} color")

class Pen(Writting_items):
    def write(self):
        print(f"im PAN -  writting {self.color} color")
    
    @staticmethod
    def _help(a, b):
        return a + b

    def __add__(self, another):
        return Pen(self._help(self.length, another.length), "yellow", "auto")

pen1 = Pen(140, "red", "auto")
pen2 = Pen(120, "green", "kolpak")
pen3 = Pen(100, "blue", "auto")
pancil1= Pencil(200, "black", "no")
pen3.write()
pancil1.write()
# print(pen1)
# print(pancil1)
# print(pen2 + pen1)


