class FLY:
	price=123		#static member
	def __init__(self):#constuctor
		self.directon="to beijing"#class member
		self.__name="leejore"#class member
		time="one hour"#local member


if  __name__=="__main__":
	print(FLY.price)
	fly=FLY()#ok
	print(fly.directon)#ok
	#print(fly.time)#error
	#print(fly.__name)#error  it is private
	print(fly._FLY__name)#ok this is always for test
      