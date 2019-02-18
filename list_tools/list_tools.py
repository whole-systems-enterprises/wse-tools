#                                                                                                                
# function to divide list into chunks                                                                            
#                                                                                                                
def chunk_a_list(the_list, chunk_size):
    for i in range(0, len(the_list), chunk_size):
        yield the_list[i:i + chunk_size]

