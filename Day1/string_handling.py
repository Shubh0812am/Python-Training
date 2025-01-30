name='abc'
name="abc"
name='''a
b
c'''

# print(name)

s = "oracle"
#print(s[-1]) #points to last character of string

#slicing 
#print(s[2:4])
#print(s[0:4:2])//0 to 4 not inclusive differnce of 2 index between slicing

#print(s[::-1]) #reverse a string completely

#print(s.upper())

p='Oracle'
#print(s.swapcase())
#print(p.swapcase())


#search
#print(s.find('e')) #first occurence index written
#print(s.find('t')) #written -1 as not present

#replace
#print(s.replace('e','l'))

t=" djf "
#print(t.strip())

#splitting
emp='Sohan, mohan, vihan' 
#names= emp.split(', ') #writtens a list 
#print(names)
#print(emp.split(', ')) #also works 


#string formatting 
name = 'sohan'
sal= 10.24
#print(f'hello your name is{name} and salary is {sal}')
print('hello your name is %s and salary is %f' %(name,sal)) #same output as previous line


