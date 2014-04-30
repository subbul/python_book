for x in xrange(1,10):
	print x


somelist = [(1,2),(2,3),(3,4)]
sum = 0
for x, y  in somelist:
	sum = sum + (x * y)

print "Sum of tuples", sum

# enumerate to get unpacked tuples

x = [1, 3, -7, 4, 9, -5, 4]
for i,n in enumerate(x): # i is index, n is the value at index
	if n < 0:
		print ("Found negative number at index ",i)


#zip stiches two or more iterables into tuples
x = [1,2,3,4]
y = ['a','b','c']
z = zip (x,y)
print "List is ",list(z)

#comprehension
x = [1,2,3,4]
squared_x = [ item * item for item in x]
#with if condition
x = [1,2,3,4]
x_squared = [item * item for item in x if item > 2]

#dictionary comprehension
x = [1,2,3,4]
x_squared_dict = {item: item * item for item in x}
print "Dictionary squared", x_squared_dict


#comparision

#AND returns first false object or the last object in comparision
print ([2] and [3,4]) #returns last object
print ( [] and [3,5]) #returns first false object -empty list

#OR returns first true object or last object

print ([] or [2] or [3]) #returns 2

#line count word count char count

infile = open('word_count.txt')
lines = infile.read().split("\n")
word_count = 0
char_count = 0

for line in lines:
	words = line.split()
	word_count += len(words)
	char_count += len(line)
print("File has {0} lines, {1} words, {2} characters".format count,word_count,char_count))
