list1=["Sam",25,"Working",7890765234,"IBM"]
list3=["Arya",20,"Student"]
print("length of the list ",len(list1))
list2=list1[0:3]
print("Creating new list from existing list ",list2)
print(list1[2:5])
list1[2]="mango"
print("After replacement ",list1)
print("Concatenating lists: ",list1+list2)
list4=[]
list4= list1.copy()
print("\n Cloning list 1 using copy function- \n", list4)
list5=[]
list5=list(list1)
print("Cloning list 1 using list function- \n", list5)

def chunkList(initialList, chunkSize):
	finalList=[]
	for i in range(0,len(initialList),chunkSize):
		finalList.append(initialList[i:i+chunkSize])
	return finalList

list6=[]
list6=chunkList(list1,2)
print("List 1 after splitting into even chunks of size 2- \n", list6)
