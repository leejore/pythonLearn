def abstract():
	raise NotImplementedError("------------------abstract---------------")


class person(object):
	"""docstring for person"""
	def __init__(self, job):
		super(person, self).__init__()
		self.job = job
		print(self.job)
		print(self.__class__ )
		if(self.__class__ is person):
			abstract()
			print("erroe-----------------")
		




class lee(person):
	"""docstring for lee"""
	__slot__='sex','age'
	def __init__(self, name,job):
		super(lee, self).__init__(job)
		self.name = name
		print(name)
		if(__class__ is lee):
			print(__class__)
			print("ok")
	
	def __getattr__(self,test):
		print("can not find")
		

	def __getattribute__ (self,test):
		print("in attribute...")
		return person.__getattribute__(self,test)


     
    	


b=lee("leejore","stu")
b.age="18"#false
b.age="shijiazhaung"#false
print(issubclass(lee,person))#true test subclass
print(isinstance(b,object))#test isinstance
print(issubclass(lee,person))#true test subclass
print(isinstance(b,object))#test isinstance
print(b.__dict__)
print(b.name1)