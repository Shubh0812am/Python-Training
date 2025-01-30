# **args and **kwargs difference 

#regular functions 
def fun(a=2,b=3):
   print(a+b)

#fun()
#lambda functions 

fun = lambda a,b : a+b 
#print(fun(10,20))


#Anonymous functions 
#print((lambda a,b: a+b) (11,22))


dobs= [4,17,9,22,24,31,10,2,4,6,9] 
# for it in dobs:
#     if it%2==0:
#         print(it)


#filter 
evens = list(filter(lambda it: it%2==0, dobs))
print(evens)

