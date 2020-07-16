#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:36:15 2020

@author: steven
"""





# create  a helper list 
helper_list = [
               "1. Add an item.",
               "2. Edit an item.",
               "3. Remove an item.",
               "4. Display all items.",
               "5. Quit.",
               "(? for  Help.)"
           
                ]

# create a list that contians all available options
available_options=["1","2","3","4","5","?"]


"""
This function executes a valid
command from the user input
"""
def execute_command(option, my_list=[]):
    
    # print helper list
    if option == '?':
        print("Help")
        for item in helper_list:
            print(item)

    # prompt to append input into myList
    elif option == '1':
        print("Add an item")
        item = input("Type in your thought...\n")
        my_list.append(item)
        
        
    # replace an item with new one
    elif option == '2':
        print("Edit an item")
        if len(my_list)==0:
            print("You have no item in your list")
        elif len(my_list)>0:
                
            num = input("Item number... ")
            # I use num - 1 here because my_list starts with index 0
            # Meaning that item # 1 is actually my_list[0]. 
            print(my_list[int(num)-1])
            
            item = input("Type in your thought...\n")
            my_list[int(num)-1] = item
            print("Replaced item # "+num)

    # pop an item in the list
    elif option == '3':
        print("Remove an item")
        if len(my_list)>0:

            num = input("Item number... ")
            print("Removed item # "+num)
            print(my_list[int(num)-1])
            my_list.pop(int(num)-1)


    # print all item in the list
    
    elif option == '4':
        print("Display all items")
        if len(my_list)==0:
            print("You have no item in your list")
            return
        i = 1
        for item in my_list:
            print(str(i) + ". " + item)
            i+=1




def todo_list():
    
    # initialize an empty list to store
    my_list=[]

    # print the helper list
    execute_command('?')
    

    #get_input()
    while True:
        option = input("Make a choice(1-5, ? for help): ")
        if option == '5':
            print("Quit")
            return
        execute_command(option, my_list)


    

def main():
    todo_list()
    

if __name__ == "__main__":
    main()
        