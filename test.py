


class lee1(object):
	def __get__(self,obj,type=None):
		print("__get__ :")
		return self.data
	

	def __set__(self,obj,val):
		print("__set__:")
		self.data=val

	def __delete__ (self,obj):
		print("__delete__:")
		del self.data



class loo(object):
	th=lee1()	
	good=90

jiji=loo()
jiji.th="kkkkkkkk"
print(jiji.th)	
del jiji.th

jiji.th="1231321"
print(jiji.th)	

            