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

available_options=["1","2","3","4","5","?"]


"""
This function executes a valid
command from the user input
"""
def execute_command(option, my_list=[]):

    if option == '?':
        print("Help")
        for item in helper_list:
            print(item)

    elif option == '1':
        print("Add an item")
        item = input("Type in your thought...\n")
        my_list.append(item)
        
        
    elif option == '2':
        print("Edit an item")
        if len(my_list)>0:
                
            try:
                num = input("Item number... ")
                print(my_list[int(num)-1])
                
                item = input("Type in your thought...\n")
                my_list[int(num)-1] = item
                print("Replaced item # "+num)
            except:
                print("Invalid Action")

    elif option == '3':
        print("Remove an item")
        if len(my_list)>0:
                
            try:
                num = input("Item number... ")
                print("Removed item # "+num)
                print(my_list[int(num)-1])
                my_list.pop(int(num)-1)
            except:
                print("Invalid Action")

    elif option == '4':
        print("Display all items")
        if len(my_list)==0:
            print("You have no item in your list")
            return
        i = 1
        for item in my_list:
            print(str(i) + ". " + item)
            i+=1





"""
This function will get a valid
user input
"""
def get_input():
    option = None
    while True:
        try:
            option = input("Make a choice(1-5, ? for help): ")
            if option in available_options:
                print()
                break
            else:
                print("Invalid input!")
        except:
            print("Invalid input!")
            continue
    return option
            
        


def todo_list():
    
    my_list=[]



    # print the helper list
    execute_command('?')
    

    #get_input()
    while True:
        option = get_input()
        if option == '5':
            print("Quit")
            return
        execute_command(option, my_list)


    

def main():
    todo_list()
    

if __name__ == "__main__":
    main()
        