list = [3, 4, 2, 9, 1, 3]
if list[0] == list[-1]:
    print("True")
else:
    print("False")

string1= "Python is a high-level, general-purpose programming language. Python is dynamically-typed and garbage-collected."

list1=[]

for word in string1:
    if word== 'Python':
        list1.append(word)

lengthstring= len(list1)

print("Slovo python je ve větě  ", lengthstring)


n=int(input("Zadej Číslo:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("Počet číslic je :",count)

x = range(-10, 5)
for n in x:
  print(n)

