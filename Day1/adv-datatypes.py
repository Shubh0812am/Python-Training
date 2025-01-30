#dictionary -> mutable , but key not duplicate

my_dict = {'eid' : 101, 'name': 'Sonu' , 'salary': 10.24}
#print(my_dict) 

my_dict['salary'] = 12.24
#print(my_dict) 

#add new value
my_dict['city']='Pune'
#print(my_dict)

#order dictionary 
from collections import OrderedDict
ord_dict = OrderedDict()

ord_dict['Sonu'] = 10 
ord_dict['Monu'] = 12.5 
ord_dict['Tonu'] = 15

# print(ord_dict)

#for k,v in ord_dict.items():
#    print(k,v)

# from collections import Counter

# chars = Counter('vamandeshmukh')
# print (chars)
    
# my_list = ['abc', 'def', 'ghi', 'jkl', 'def', 'ghi', 'def', 'ghi', 'jkl', 'jkl']
# count = Counter(my_list)
# print(count)

#chainMap 

from collections import ChainMap 

my_list1 = {'Sonu': 10.25, 'Monu': 12.50} 
my_list2 = {'Tonu': 15.50, 'Sonu': 11.50} 

dicts = ChainMap(my_list1,my_list2) 
#print(dicts)
#print(dicts['Sonu']) #print the first occurence of sonu values


#named tuple -> lightweight objects, immutable
from collections import namedtuple
Emp = namedtuple('Emp',['eid', 'name', 'salary'])
emp1 = Emp(101,'Sonu',10.25)
emp2 = Emp(102,'Monu',12.25)

print(emp1.name,emp1.salary)