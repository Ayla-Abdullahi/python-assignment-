#list declaration
My_list=[]

# insertion of values in My_list
My_list.append(10)
My_list.append(20)
My_list.append(30)
My_list.append(40)

#inserting a value in a specific position
My_list.insert(1,15)

#extending the list with multiple values
My_list.extend([50, 60, 70])

#removing the last element in the list
My_list.pop()

#sorting the list in an ascending order
My_list.sort()

#finding the index of a specific value
Index_30=My_list.index(30)

#displaying the status of the list and the index of 30
print("status of my list:",My_list)
print("Index of 30:",Index_30)