class Computer :
    count = 0
    def __init__ (self , ram , hard , cpu):
        self.ram = ram 
        self.hard = hard
        self.cpu = cpu
    def value (self) :
        return self.ram + self.hard + self.cpu
class laptop(Computer) :
    def value (self) :
        return self.ram + self.hard + self.cpu+ self.size
    

ps1 = Computer(4,0.5,2)

print(ps1.value())

 
laptop1 = laptop(16, 1, 9)
laptop1.size = 13
print (laptop1.value())
