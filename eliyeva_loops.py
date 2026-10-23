#1 
for i in range(10,0,-1):
    print(i)
print('liftoff!')


#2 
forchild=0
foradult=0
for i in range (1 ,6):
    age=int(input())
    if age<18 :
        forchild +=1
    else:
        foradult +=1
    print('age of visitor ', i , ":'". age )
print("child tickets:" , forchild)
print('adult tickets: ' , foradult )


#3 dediler ki run eleme
for i in range(1,10,2):
    print(i , end=' ')


#4
total=0