class cse:
    def __init__(self, name):
        print(f"Details of {name}")
        self.dsa = int(input("DSA : "))
        self.py = int(input("PYTHON : "))
        self.java = int(input("JAVA : "))

    def total(self):
        return (self.dsa + self.py+ self.java)

    def avg(self):
        return self.total() / 3


narasimha = cse("NARASHIMA")
yuvaraj = cse("yuvaraj")
pavan = cse("pavan")

print("Narasimha Total is",narasimha.total())
print("Narasimha Average is",narasimha.avg())

print("Yuvaraj Total is",yuvaraj.total())
print("Yuvaraj Average is",yuvaraj.avg())

print("Pavan Total is",pavan.total())
print("Pavan Average is",pavan.avg())
