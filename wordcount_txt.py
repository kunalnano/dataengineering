import wget

url = 'http://www.gutenberg.org/files/1342/1342-0.txt'
file_name = wget.download(url)

word_count = 0

with open(file_name,'r') as file:
	for line in file:
		word_count += len(line.split())

print ("number of words : ",word_count)
