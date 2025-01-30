berth = ['lower','middle','upper','sidelower','sideupper'] 

#using loop
#for i in range(1,72):
#    print(berth[(i-1)%5])

#using user input
berth_no = int(input())
print(berth[(berth_no-1)%5])
