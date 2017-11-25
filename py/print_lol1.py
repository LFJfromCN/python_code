def print_lol1(the_list,indent=False,level=0):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol1(each_item,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):   
                    print '\t'
            print(each_item)


movies = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
        ["Graham Chapman",
 
    ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print_lol1(movies,True)
