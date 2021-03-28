
"""
Class ListKeeper

Keeps a dictionary of lists and provides some methods to operate on the items 
"""
class ListKeeper:
    """
    There are no private variables in Python, but vars starting with __ are a bit protected 
    by via renaming through the interpreter (not a security feature!)
    """
    __listDict = dict()
    
    """
    __init__()
    Constructor
    """
    def __init__(self):
        self.__listDict['example'] = [1,2,3,4,5]
    
    """
    show()
    returns the names (= keys) of all dict items 
    """
    def show(self):
        return self.__listDict.keys()
    
    """
    add()
    adds new list to dict
    """
    def add(self,name, newList):
        self.__listDict[name] = newList
    
    """
    delete()
    deletes list from dict
    """
    def delete(self, name):
        self.__listDict.pop(name)
    
    """
    sort()
    sorts list of given name
    """
    def sort(self, name):
        self.__listDict[name].sort()
    
    """
    append()
    appends list to existing entry
    """
    def append(self, name, appList):
        self.__listDict[name].extend(appList)
        
    """
    __getitem__()
    overwrites the [] operator
    """    
    def __getitem__(self, key):
        return self.__listDict[key]
        
