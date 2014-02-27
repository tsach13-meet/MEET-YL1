class Integer(object) :
	def __init__(self, num_to_set)
		self.num = num_to_set
	
	def display(self):
		return self.num 

if __name__=="__main__":
	num1 = Integer(25)
	num1.display()	
