import sys
def main():
	contents = sys.stdin.read()
	sys.stdout.write(contents.replace(sys.argv[1],sys.argv[2]))
	#  python program_replace.py 0 zero 
	# 0 will be replaced by string "zero"
	# enter 1 2 3 0.. by pressing ctrl-z in win, check 0 is replaced by ZERO

main()