file = open('codingal.txt')
print(file.read())
file.close()

file_read = open('codingal.txt', 'r')
print("file in read mode-")
print(file_read.read())
file_read.close()

file_write= open('codingal.txt', 'w')

file_write.write("file in write mode...")
file_write.write("hi!! I am a chicken. I am 2 years old")
file_write.close()

file_append = open('codingal.txt', 'a')
file_append.write("\n file in read mode ....")
file_append.write("anshul see append mode")
file_append.close()

file = open('codingal.txt')
counter =0

content = file.read()

colist= content.split("\n")

for i in colist:
    if i:
        counter +=1

print("This is the number of lines in the file ")
print(counter)

firstfile = input("Enter the name of the first file:")
secondfile= input("Enter the name of the scond file:")

f2 = open(secondfile, 'r')
data = f2.read()
f2.close

f1= open(firstfile, 'a')
f1.write(data)
f1.close()

print("content of", secondfile, "has been added to", firstfile)
