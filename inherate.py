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
			
		


class lee(person):
			"""docstring for lee"""
			def __init__(self, name,job):
				super(lee, self).__init__(job)
				self.name = name
				print(name)
				if(__class__ is lee):
					print(__class__)
					print("ok")
						


b=lee("leejore","stu")
