""" my math -- math function """
pi = 3.1413
def area(r):
    """area(r) finds the area with given radius r """
    global pi
    return  ( pi * r * r)


def functionx(x):
	return x

#methods with _ (underscore) will not be exposed, even import * ,
#these are private functions
def _functiony(y):
	return y

#use locals() in shell to list all local variables visible
#gloabls() results in dictionary of global variables


#dir gives dir(module) list of functions in a module
#print(max.__doc__) prints the help of max method


#standard methods like "list" can be overriden locally
list = ['a','b','c'] # you will not be able to use default list until you "del" list  overriden

