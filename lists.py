simple_list = [1,2,3] 
print "Simple List",simple_list
hetero_list = [1,"Helo",[100,200,300]]# can containheterogenous values
print "Original List",hetero_list
print  "Type of object hetero_list",type(hetero_list) # type of object, shows its fundamental data type, for e.g., here it is LIST 
print "Item at index 0 ",hetero_list[0] #first index
print "Item at index -1",hetero_list[-1] #negative index start from end so here the last elemtn in LIST
print "Length -->", len(hetero_list)

print "#############################################"
big_list = [1,2,3,4,5,6,7,8,9]
print " big List", big_list
print "lets slice from index [2:]",big_list[2:] # start, end index, includes start, ends before end-index
print " slice till [:4]", big_list[:4] # stops before index 4 , 0-1-2-3

new_list = big_list[:] #from beginning to end
print "New list is a copy of big list", new_list

print "##############################################"
big_list = [1,2,3,4,5,6,7,8,9]
big_list[2]="x"
print " Index 2 is modified to x-->"
print big_list

big_list[len(big_list):] = [11,12,13] # adding at the end  appending

print "Appended list", big_list

print " Append vs Extend list"

list_a = [1,2,3]
list_b = ['a','b','c']
print "list a", list_a
print "list b", list_b

list_a.append(list_b)
print "Append b to a", list_a

list_a = [1,2,3]
list_a.extend(list_b)
print "Extend b to a", list_a

list_a = [1,2,3]
print "Original list", list_a
list_a.insert(1,"x")
print " x insert before index 1",list_a

list_a = [1,2,3]
list_a.reverse()
print "reverse list", list_a


print "1 in list_a", (1 in list_a)
print "10 in list_a", (10 in list_a)

print "###################################################"
def custom_sort(string1):
	return len(string1)

list_a = ["I am","good","World","Very big statement"]
list_a.sort()
print "Sorted naturally alphabetical", list_a
list_a = ["I am","good","World","Very big statement"]
list_a.sort(key=custom_sort)
print "Sorted using custom key", list_a

list_a = [10] * 4
print "list with  initialization using *", list_a
list_a = [1,11] * 4
print "list with  initialization using *", list_a
list_a = [10,20,30,40,50,60]
print "List -->", list_a
print "Index of 40-->", list_a.index(40)

list_a = [20,2,442,3,2,67,3]
print "List -->", list_a
print "Count occurance of 3 in list ==",list_a.count(3)