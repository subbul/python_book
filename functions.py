""" returns the power of x to y
"""
def power(x,y=2):
	r = 1
	while y > 0:
		r = r * x
		y = y - 1
	return r


# passing arguments by parameter name
pwer(y=10,x = 2)


#variable number of arguments prefixing variable with "*" will collect all the arguments
# as a tuple

def maxnum(*numbers):
	if len(numbers) == 0:
		return None
	else:
		maxnum = numbers[0]
		for n in numbers[1:]:
			if n > maxnum:
				maxnum = n
		return maxnum

#call the function
maxnum(10,1210,242,255,988)


#multiple arguments with keyword will be captured by prefixing "**" to variable
# and the collection will be dictionary with keyword as key 

def example_fun	(x,y, **other):
	print("x:{0}, y:{1}, keys in  'other':{2}".format(x,y,list(other.keys())))
	other_total = 0
	for k in other.keys():
		other_total = other_total + other[k]
	print("The total of values in 'other' is {0}".format(other_total))


#call method using
example_fun(2,y="1",foo=3,bar=4)


#mutable objects as arguments
def f(n,list1,list2):	
	list1.append(3) # modifying onriginally passed list
	list2 = [4,5,6] # creating new reference, doesn't affect "Z" originally passed
	n = n + 1 # new reference not modified


x = 5
y = [1,2]
z = [4,5]

f(x,y,z)
print "x,y,z", x,y,z


#global variable

def fun():
	global a #affects global scope
	a = 10
	b = 20


a = 100
b = 200
print "a and b", a,b
fun()
print " after calling fun  a & b", a,b


#assigning fucntions to variable

def f_to_kelvin(degrees_f):
	return 273.15 + (degrees_f - 32 ) * 5 /9

def c_to_kelvin(degrees_c):
	return 273.15 + degrees_c

abs_temperature = f_to_kelvin
abs_temperature(32)

abs_temperature = c_to_kelvin
abs_temperature(0)


#assigning in dictionary

func_dict = {'FtoK':f_to_kelvin,'CtoK':c_to_kelvin}

func_dict['FtoK'](32)

#lambda or inline or anonymous fucntions

func_dict = {'FtoK':lambda deg_f: 273.15 + (deg_f - 32 ) *5 /9, \
			 'CtoK': lambda deg_c: 273.15 + deg_c }


#generator function, useful for iteration
#local variable is preserved across function calls
# yield will return failure if condition fails
def skip_by_one():
	x = 0
	while x < 10:
		print ("in generator x=",x)
		yield x
		x += 2


for i in skip_by_one():
	print(i)


20 in skip_by_one() #should return false



#decorators.. Function A takes argument function B, wraps B within C and returns C
#useful in adding some pre-processing to an existing functions
def decorate(func):
	print (" in decorate function, decorating",func.__name__)
	def wrapper_func(* args):
		print ("executing",func.__name__)
		return func(*args)
	return wrapper_func

@decorate
def myfunction(parameter):
	print(parameter)

myfunction("hello")