class Temprature:
    """
    A class temprature is repesent final data of report and update 
    data according parameter values.
    ...
    Attributes
    ----------
    maximum_list : string
        All max values in file
    minmum_list : string
        all min values in file
    no_of_lines : int
        no of orws in column

    Methods
    -------
    __init__(self): 
    set_maximum_list(self,val):
        set maximum_list with val  
    set_minimum_list(self,val):
        set minimum_list with val  
    set_no_of_lines(self,val):
        set no_lines with val   
    display_report(self):
        Print report    
    """
    def __init__(self):
        """
        Construct all the necessary attributes for the file data

        Parameters
        ----------
        maximum_list : string list
            store a column of max temprature from file
        minimum_list : string list
            store a column of max temprature from file
        no_of_line : int
            no of rows in column
       
        Return
        ------
        None     
        """
        self.maximum_list = []
        self.minimum_list = []
        self.no_of_lines = 0
        

    def set_maximum_list(self,val):
        """
        set maximum_list with val(val is the list of max temprature).

        Parameter
        ---------
        val : string
            list of max temprature

        Return:
        None

        """
        self.maximum_list = val

    def set_minimum_list(self,val):
        """
        set minimum_list with val(val is the list of min temprature).

        Parameter
        ---------
        val : string
            list of min temprature

        Return:
        None
            
        """
        self.minimum_list = val

    def set_no_of_lines(self,val):
        """
        set no_of_lines with val(val is the no rows in  column).

        Parameter
        ---------
        val : int
            No of rows

        Return:
        None
            
        """
        self.no_of_lines = val


    def display_report(self):
        """
        Print report

        Parameter
        ---------
        None 

        Return:
        None
            
        """
        index_number = 0
        sym='+'
        max_range = 0
        min_range = 0
        for i in range(self.no_of_lines - 1):

            if(self.maximum_list[index_number].isdigit()):
                #here is the check for checking number
                max_range = int(self.maximum_list[index_number])
            else:
                max_range = 0    

            if self.minimum_list[index_number].isdigit():
                min_range = int(self.minimum_list[index_number]) 
            else:
                min_range = 0      
            print(index_number,end='')
            for j in range(max_range):
                print("\033[1;34;40m" + sym, end='' )
            print(str(max_range) + "C")
            print("\033[1;37;40m")
            print(index_number,end='')
            for j in range(min_range):
                print("\033[1;31;40m"+sym,end='')
            print(str(min_range)+"C")
            print("\033[1;37;40m")       
            index_number = index_number + 1    
