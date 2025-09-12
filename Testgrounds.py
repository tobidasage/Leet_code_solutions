
name:str = 'oluwatobi'

book:dict = {'a':2, 'b':3, 'c':8}

book2:dict = {}



for i in range(len(name)):
    book2[name[i]] = 1 + book2.get(name[i], 0)
    

    
