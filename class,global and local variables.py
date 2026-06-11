class Animal:
        #class variable
	x = 1
	z=100
	
	def __init__(self):
                #instance variable
		self.x = 22
		self.y = 5

		#local variable
		x = 30
		z = 40
		t= 95
		print("Local variable x = " ,x)
		print(self.x + x)
		
	    
print("Printing the class variable throgh the the class name: x = " ,Animal.x)
n = Animal()

print("Instance variable x will be printed (not the class variable x) x = " ,n.x)

print("Printing the class variable throgh the object: x = " ,n.z)
#print(Animal.t)   #=>type object 'Animal' has no attribute 't'


