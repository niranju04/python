#list
lst=[1,2,3]
print(len(lst)) #length of the list
lst.append(4)#add elemnt in end
print(lst)
lst.insert(0,5)#add element in index
print(lst)
lst.extend([6,7,8,9])#add multiple element
print(lst)
lst.remove(3)#delete
print(lst)
lst.pop(0)#delete index
print(lst)
lst.sort()#arrange in AO
print(lst)
lst.sort(reverse=True)#arrange in Do
print(lst)

#tuple
tup=(1,2,3)
print(len(tup))
print(max(tup))
print(min(tup))
print(tup[0])
tup=tuple("hello")
print(tup)

#dict
d={0:"hello",1:"hii"}
print(d[0])
for i in d:
    print(i,d[i])
d[2]="heyy"
print(d)
del d[1]
print(d)
print(d.keys())
print(d.values())
e={3:"welcome",4:"everyonr"}
d.update(e)
print(d)

#sets
s={1,2,3}
print(s)
s.add(4)
print(s)
print(len(s))
print(max(s))
print(min(s))
s.remove(2)
print(s)
ss={3,4,5}
s.update(ss)
print(s)

#stud marks dict
stu={
    "name":"vaishu","age":23,"dept":"CSE","marks":[90,67,45,98]
}
print("Student name:",stu["name"])
print("Student age:",stu["age"])
print("Student dept:",stu["dept"])
print("Student marks:",stu["marks"])

#word frequency counter
word = {}
text = "hello world hello"
words = text.split()
for wrd in words:
    word[wrd] = word.get(wrd, 0) + 1
print(word)