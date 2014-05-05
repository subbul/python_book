import fileinput
def main():
	for line in fileinput.input():
		if not line.startswith('##'):
			print(line,end="")

main()

#call program with dat1.txt dat2.txt (it will be stripped with lines starting with ##)