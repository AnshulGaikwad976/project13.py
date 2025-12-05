file= open('doc.txt' ,'r')
print(file.read())
file.close()

file = open('doc.txt', 'r')
print("\n read in parts \n")
print(file.read(8))
file.close()

file = open('doc.txt', 'a')

file.write("hi i am a penguin and iam 1year old")
file.close()

file1 = open('codingal.txt',
                      'r')
file2 = open('codingalupdated.txt',
                      'w')

for line in file1.readlines():


    if not (line.startswith('coding')):
        print(line)
        file2.write(line)

file2.close()
file1.close()    

fn = open('codingal.txt' ,'r')
fn1 = open('codingalupdated.txt', 'w')

cont = fn.readlines()
type(cont)
for i in range(1 ,len(cont)+1):
    if(i %2 !=0):
        fn1.write(cont[i - 1])

    else :
             pass

fn1.close()
fn1=open('codingalupdated.txt', 'r')

con1 = fn1.read()

print(con1)

file_read = open('codingal.txt', 'r')
print("file in read mode-")
file_read.close()

file_write = open('codingal.txt' ,'w')
file_write.write("hi iam a pngu")
file_write.close()

file_append = open('codingal.txt', 'a')
file_append.write("\n file in append mode")
file_append.write("i am a pingu and i am 2years old")
file_append.close()