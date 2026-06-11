class Test:
    def __init__(self,newValue):
        self.a = newValue

    def __add__(self,other):
        return self.a + other.a

    def __sub__(self,other):
        return self.a - other.a

    def __repr__(self):   # the same as __str__
        return "a= " + str(self.a)

#Shared References
#Testing if References are Aliases
reg1 = Test(12)
reg2 = reg1

#if it's True the the variables are aliases
print(reg1 is reg2)
#if it's True Checking the data contained within objects are equal
#means self.a for both are equal
print(reg1 == reg2)

print()

reg3 = Test(12)
print(reg1 is reg3)
print(reg1 == reg2)

print()

reg4 = Test(22)
print(reg1 is reg4)
print(reg1 == reg4)  #=> __eq__ will be called

print()

reg1.a = 100
print("reg2.a=", reg2.a)
print("reg3.a=", reg3.a)
print("reg4.a=", reg4.a)

print("reg1 + reg4=",reg1+reg4)
print("reg1 - reg4=",reg1-reg4)
print(reg1)

print()
#Checking Type
age = 18
print(isinstance(age,int))
print(isinstance(age,str))
