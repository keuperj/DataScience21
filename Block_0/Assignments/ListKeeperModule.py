# ***********************
# Program Name: ListKeeper - Block 0
# Author: Daniel Hin 181379 MMR
# Date: 22.03.2021
# Purpose: Assignment 1
# Description: Class ListKeeper stores named lists
# ***********************

class ListKeeper:
    # initialize class ListKeeper with default dictionarie
    def __init__(self):
        self.keeperdict = {
        'names': ['example'],
        'lists': [[1,2,3,4,5]]}
        
    # returns all list names   
    def show(self):   
        return self.keeperdict["names"]
    
    # adds a new list
    def add(self,new_name,new_list):
        self.keeperdict["names"].append(new_name) 
        self.keeperdict["lists"].append(new_list)
        
    # delets list    
    def delet(self,del_name):
        index = self.keeperdict["names"].index(del_name)
        self.keeperdict["names"].pop(index)      
        self.keeperdict["lists"].pop(index)
        
    # returns the sorted list 'sort_name'    
    def sort(self,sort_name):
        index = self.keeperdict["names"].index(sort_name)
        self.keeperdict["lists"][index].sort()
        return self.keeperdict["lists"][index]
    
    # appends list to name
    def append(self,name,app_list):
        index = self.keeperdict["names"].index(name)
        self.keeperdict["lists"][index].extend(app_list)
        
    # extra print function for functionality tests
    def print_dict(self):   
        print(self.keeperdict)
     
        
        