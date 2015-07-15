class room(object):
	personCount=0
	
			
	def __init__(self,name):
		def sayHi():
			print("hello,I am ",name)
		self.name=name
		room.personCount=room.personCount+1
		print("inition your name is :",name," used  room :" ,room.personCount)
		sayHi()
		
	
	def __del__(self):
		print("bye ",self.name)
		room.personCount=room.personCount-1
		if(room.personCount==0):
			print("the romm is empty")
		else:
			print("the room still have ",room.personCount)

	
	def __setitem__(self,key,value):
		
		print((key,value))

	
	def __getitem__(self,key):
		print("i am finding")

	
	def __eq__(self,another):
		print("compare two instance ")
		return False


	def __delitem__(self,key):
		print("del is called")

	

	def testForDynamic(self):
		print("in the class")
			

	
	

	
def dynamicFuction(pp):
	print("out the class")
if(__name__=="__main__"):
	room1=room("leejore")
	room2=room("lucy")
	room2['10']='100'
	room2['10']
	del room1["pp"]
	if(room2==room1):
		print("they are equal")


	room2.testForDynamic=dynamicFuction

	room2.testForDynamic(room2)
		