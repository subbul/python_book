from optparse import OptionParser

def main():
	parser = OptionParser()
	parser.add_option("-f","--file",dest = "filename",help="write report to FILE",metavar="FILE")
	parser.add_option("-x","--xray",dest ="xray",help="specify xray strength")
	parser.add_option("-q","--quiet",action="store_false",dest="verbose",default=True,help="don't print status message to stdout")

	(options,args) = parser.parse_args()
#provide command line like this
# python program_parseopt.py -x100 -f infile -q arg1 arg2 or python program_parseopt.py --help
# options are -x=100, -f= infile
# arguments, positional , arg1, arg2 comes after options
# invalid options like "-r" will be rejected
	print("Options are:",str(options))
	print("Arguments are:",args)

main()