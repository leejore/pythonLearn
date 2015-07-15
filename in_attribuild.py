class father(object):
	"fathe class"
	def __init__(self):
		"constructor of father"
		self.built="father bulid"


class son(father):
	"inherate from father "
	def accept(self):
		self.acceptAttend="this is method in the attribute"
		return self.acceptAttend
	@staticmethod
	def staticmethodTest():
		print("I am staticmethod ,define by @staticmethod")
	

	def __privateMethodForCastToStatic():
		print("I am private method,I can cast to staticmethod by staticmethod() fuction ")


	def normalMemberMethod():
		print("I am normalMemberMethod,I can cast to staticmethod by staticmethod() ,too")
	castPrivateMethodToStatic=staticmethod(__privateMethodForCastToStatic)
	castNormalMethodToStatic=staticmethod(normalMemberMethod)
	@classmethod#use defult cls
	def class_methodTest(cls,mycls):
		print("classmethod:",cls,mycls)

if(__name__=="__main__"):
	fatherClass=father()
	sonClass=son()
	print("this is the attribute inherate from father :",sonClass.built)
	print("this is the father __base__ : ",father.__base__)#ouput tuple
	print("this is the son __base__ : ",son.__base__)
	print("in attribute __dict__ : ",father.__dict__)#output attribute dict
	print("in attribute __dict__ : ",son.__dict__)
	print("in attribute __module__ : ",father.__module__)#output module name
	print("in attribute __module__ : ",son.__module__)
	print("in attribute __name__ : ",father.__name__)#class name
	print("in attribute __name__ : ",son.__name__)
	print(sonClass.accept())	
	sonClass.staticmethodTest()
	sonClass.castNormalMethodToStatic()
	sonClass.class_methodTest("leejore")


