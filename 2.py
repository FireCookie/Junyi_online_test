input_string = raw_input()
max_number = int(input_string)
number_list = range(1,int(input_string)+ 1)

for i in range(1,max_number/3):
    if (i * 3) % 5 != 0:
        number_list.remove( i*3 )
        
for i in range(1,max_number/5):
    if (i * 5) % 3 != 0:
        number_list.remove( i*5 )
        
print len(number_list)