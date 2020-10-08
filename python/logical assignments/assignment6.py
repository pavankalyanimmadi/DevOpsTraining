'''
Created on Oct 8, 2020

@author: Immadi pavan kalyan
'''


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total+=v;
        print(str(v)+" "+k)
        
    print("Total number of items: " + str(item_total))
    
    

def addToInventory(inventory, addedItems):
    updatedInventory=dict(inventory);
    for x in addedItems:
        
        for k,v in inventory.items():
            if(k==x):
                updatedInventory[k]+=1;
                break;
            
            updatedInventory[x]=1; 
            
    return updatedInventory;   
            
            
    
 
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
