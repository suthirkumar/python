''' B) Write a program which reads content from one file (File 2) and
add the content to another file (File 1)
'''

f1="sample.txt"
f2="sample2.txt"
start=open(f1,'a')
end=open(f2,'r')
content=end.read()
start.write(content)
start=open(f1,'r')
print(start.read())
