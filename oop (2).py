class person :
    count = 0
    def __init__ (self, name ,age):
        self.name = name
        self.age = age
    def get_name(self):
        print('name is %s' % self.name)     
    def get_age(self):
        print('age is %s' % self.age)
    def get_info(self):
        print ('name is %s and age is %i' %(self.name ,self.age))
    def get_happy(self) :
        self.age = self.age + 1
        print(' %s hppey birthday age %s '  % (self.name  , self.age ))
mohammad=person('mohammad' , 14)
mohammad.get_name()
mohammad.get_age()
mohammad.get_info()
mohammad.get_happy()
ali= person('alimotahari', 15)
ali.get_info()