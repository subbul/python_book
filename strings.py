##strings are sequence of characters

x = "Hello World"
print "x at 4","'",x[4],"'"

print "x from x[5:]",x[5:]
print "Length of string", len(x)
x = "hello"
y = "World"
print "x + y", x+y
print "With escape sequence \\ \""
print "octal value \115"
print "Hex value \x6D"

#string object are immutable, so string methods return new string rather than modifying original

#split and join
#split use white space as delimiter

print "Join-->", " ".join(["join","puts","space","between","words"])
print "Join with #-->", "#".join(["Seperated","with","colons"])
print "Join with nothing-->", "".join(["Seperated","with","Nothing"])
x = "You can \t\t have white spaces \n new lines and other spaces"
print " Split string" ,x.split()
x = "Mississipi"
print "Misssipi split with ss", x.split("ss")
print "split with parameters"
x = "a b c d"
print "1 split",x.split(' ',1)
print "2 split",x.split(' ',2)
print "3 split",x.split(' ',3)

## convrting string to numbers vice-versa

print "float-->",float("1234.56")
#should throw an error print "int-->",int("123.45")
x  = "   Hello world \t\t"
print "Strip spaces", x.strip()
print "Left strip",x.lstrip()
print "Right strip",x.rstrip()


#strip particular characters
x = "www.python.org"
print "Stripped w -->" , x.strip("w")
print "Stripped gor. -->" , x.strip("wgor.")