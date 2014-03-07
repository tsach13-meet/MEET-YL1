class Integer(object) :
	def __init__(self, num_to_set, p_n):
		self.num = num_to_set
		self.p_n = p_n
	def display(self):
		print str (self.num )+ " " +self.p_n


class NegativeInteger( Integer) :
	def __init__(self, num_to_set):
		super(NegativeInteger, self).__init__(num_to_set,"negative")	
		
	def display(self):
		Integer.display(self)
		text = "This is an object of the NegativeInteger class"
		print text

if __name__=="__main__":
	
	num_of_nums = raw_input("how many numbers you want to create?")
	num_of_nums = int(num_of_nums)
	for y in range(num_of_nums) :
		p_or_n = raw_input("do you want it to be p or n?") 
		x = raw_input("what is the number?")
		x = int(x)
		x = Integer(x, p_or_n)
		x.display()
	

	# num1 = raw_input("give me please positive number")
	# num1 = int(num1)
	# num2 = raw_input("give me please negative number")
	# num2 = int(num2)
	# num1 = Integer(num1, "positive")
	# num2 = 	NegativeInteger(num2)	
	# list1 = [num1,num2]
	# for x in list1:
	# 	x.display()



	# num_of_p_nums = raw_input("how many positive numbers you want to create?")
	# num_of_p_nums = int(num_of_p_nums)
	# for y in range(num_of_p_nums) :
	# 	p = raw_input("give me please positive numbers")
	# 	p = int(p)
	# 	p = Integer(p,"positive")
	# 	p.display()
	# 