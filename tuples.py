print "######################TUPLES######################"
x = ('a','b','c','d') # tuples are covered with paranthesis ( )
print "Tuple -->", x
print "Type of x-->",type(x)
x = 3
y = 4
z = (x+y,) #, within () indicates one element Tuple
print "Z is -->", z

print "(a,b,c,d) = (1,2,3,4)"
(a,b,c,d) = (1,2,3,4) #unpacking

print " c is -->", c

var1 = 10
var2 = 20
print "Var 1 and var2 before swap", var1,var2
var1,var2 = var2, var1
print "Var 1 and var2 after swap", var1,var2


print "###############sets#############################"
x = set([1,2,3,1,3,4,5])
print "Set is -->",x # removes duplicates, only unique values are retained

x.add(10)
print "X after adding 10", x
x.remove(1)
print "X after removing 1",x
x = set([1,2,3,4])
y = set([1,5,6,7])

print "x-->",x,"y-->",y
print "X or Y",x | y #Union
print " X and Y", x & y #intersection
print " X ^ Y", x ^ y # x-or
