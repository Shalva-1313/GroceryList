#empty dictionary that will become the list
groceryList = {}   

i=1
while True:
        try:
            item = input()
            #changes format of input to title case so it matches keys in the dictionary
            dictitem = item.upper() 
            
            #will add each new item inputted to the dict groceryList
            if dictitem in groceryList:  
                #will update # of same item entered
                groceryList.update({dictitem:i+1})  
                
            #will update the first time an item is entered.
            else:
                groceryList.update({dictitem:i}) 
                
        #ends program when user is done with order and hits control D
        except (EOFError):                       
            i=0
            break
print()

#key is the number of times an item is entered and the value is the item
for key in sorted(groceryList.keys()):
    print(groceryList[key], key)
   
