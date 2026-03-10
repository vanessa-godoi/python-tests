file = open ('textfile.txt', 'w')

file.write ('Python Course \n')
file.write ('Practical CLass')
file.close()

#text file reading

reading = open ('textfile.txt', 'r')
print(reading.read())
reading.close()