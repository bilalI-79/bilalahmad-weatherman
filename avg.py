class Average:
    """
    A class to represent the find average 

    Attributes
    ----------
    None

    Method
    ------
    find_avarage(self,lst ,no_of_line):
        return average of list
    """
    def __init__(self):
        pass

    def find_avarage(self,lst ,no_of_line):
        """
        Find average of list

        Parameter
        ---------
        lst : string
            list of string values
        no_of_lines : int 
            no of rows in column


        Return
        ------
            returns the average of list        
        """
        j=0
        temp_list=[]
        for i in range(no_of_line - 1):
            if lst[j].isdigit():
                temp_list.append(int(lst[j]))
            j = j + 1
        avg = sum(temp_list) / no_of_line
        return avg 