list = []
dictionary = {}

# list[0]='hello'// not allowed
dictionary[0]='hello' #allowed
dictionary["two"]= 2
dictionary["pi"]= 3.14

# literal use of  python dictionary 
english_to_french = {}
english_to_french['red'] = 'rouge'
english_to_french['blue'] = 'bleu'

english_to_french = {'red':'rouge','blue':'bleu','green','vert'} # another representation of name value pairs

print "Length of dictionary english_to_french", len(english_to_french)

print "Keys of dictionary", english_to_french.keys()
print "Values of dictionary", english_to_french.values()
print " Items of dictionary, name:value pairs", english_to_french.items()
del english_to_french['green']
print " Items after del green", list(english_to_french.items())	# converting from view to list otherwise
#iterations will be difficult

print "Is Red in Dictionary?-->", "red" in english_to_french
print "Is yellow in Dictionary? -->", "yellow" in english_to_french

# dictionary.get (search, string_if_search_string_not_found)
print "Result of query if red is available?",english_to_french.get("red","red not available")
print "Result of query if yello is available?",english_to_french.get("yellow","yellow not available")
english_to_french.setdefault('yellow','defaultyellow') #check if yellow has value, if not set defaultyellow


#update

z = {1:'One',2:'Two'}
x = {0:'Zero',1:'one'}
print " Z is -->",z.items()
print " X is -->",x.items()

x.update(z)
print " Updated X",x.items()

#word counting

sample_string = "to be or not to be"
occurence = {}
for word in sample_string.split():
	occurence[word] = occurence.get(word,0)+1

for word in occurence:
	print ("The word is occuring ",occuring[word],"times")


#sparse matrix contain only non-zero items
matrix = { (0,0):3, (0,2):-2,(0,3):11,(1,1):9,(2,1): 7 ,(3,3):-5}

matrix.get((rownum,colnum),0)

#dictionary for caching
