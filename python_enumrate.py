# enumrate by default gives index so we can use that one 
 
mylist=[10,52,48,59,34,56,87,45]

for i,element in enumerate(mylist):
    if i%2==0:
        print(f"{i}:{element}")










# .join() function...     #...applicable only on string and gives only one string as a output

name=["sanidhya","prem","om","tom","deepak"]
new="@gmail.com ".join(name)
print(new)
# print(new.split())

# marks=[12,14,16,19,10,14,13,7]
# new_marks="%".join([str(i) for i in marks])