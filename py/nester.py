def print_lol(the_list,level):
    """This function takes a positional argument called "the_list",which
is any Python list (of-possibly-nested lists).Each data item in the provided list is (recursively)
printed to the screen on it's own line.A second argument called "level" is used to insert tab-stops
when a nested list is encountered."""
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            for tab_stop in range(level):
                print "\t"
            print(each_item)
