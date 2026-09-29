class Person:

	def __init__(self,phone = "444-444-444", adress = "123 Fake Street", name = "none"):

		self.phone = phone
		self.adress = adress
		self.name = name


	def death(self):
		
		print("DATH")

	def set_name(self,new_name):

		self.name = new_name

	def get_name(self):

		return self.name


