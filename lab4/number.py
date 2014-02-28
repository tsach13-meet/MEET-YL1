class Integer(object) :
	def __init__(self, num_to_set, p_n):
		self.num = num_to_set
		self.p_n = p_n
	def display(self):
		return str (self.num )+ " " +self.p_n


class NegativeInteger( Integer) :
	def __init__(self, num_to_set):
		super(NegativeInteger, self).__init__(num_to_set,"negative")	

if __name__=="__main__":
	num1 = Integer(25,"negative")
	print num1.display()	
	num2 = NegativeInteger(12)