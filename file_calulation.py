class File:
    """
    A class to represent the file related work. or extract required data
    from file.
    ...
    Attributes
    ----------
    list_of_max : string list
        store a column of max temprature from file
    list_of_min : string list
        store a column of max temprature from file
    no_of_line : int
        no of rows in column
    month_name : str
        name of month
    file_data = string
        whole data of file  

    Methods
    -------
    change_file_into_readable(self, file_pointer):
        read the file and return in the form of list  
    find_maximum_list_from_file(self): 
        extract max temprature from file
    find_minimum_list_from_file(self):
        extract min temprature from file
    convert_number_into_month(self,val):
        return month name  
    dsiplay_file_data(self):
        print file data   
    get_max_list(self):
        return max list    
    def get_min_list(self):
        retune min list
    def get_whole_data_of_file(self):   
        return alll the data of file
    def get_month(self):         
        return month name
    def get_no_of_lines(self):
        return no of rows in column    
    """
    def __init__(self):
        """
        Construct all the necessary attributes for the file data

        Parameters
        ----------
        list_of_max : string list
            store a column of max temprature from file
        list_of_min : string list
            store a column of max temprature from file
        no_of_line : int
            no of rows in column
        month_name : str
            name of month
        file_data = string
            whole data of file 

        Return
        ------
        None     
        """
        self.list_of_max = []
        self.list_of_min = []
        self.no_of_lines = 0
        self.month_name="no month"
        self.file_data = []
 
    def change_file_into_readable(self, file_pointer): 
        """
        This function will read file and append line by line in list so that 
        we access to data easily

        Parameter
        ---------
        file_pointer : file 

        Return
        ------
        None
        at the end of function list assign to file_data and count no of rows 
        also which is assigng to no_of-lines
        """
        file_read = file_pointer.readlines() 
        temp = []
        line_count = 0
        for i in range(len(file_read)):
            temp.append(file_read[line_count].split(","))
            line_count = line_count + 1    
        self.file_data = temp
        self.no_of_lines = line_count

    
    def find_maximum_list_from_file(self):
        """
        This function is to extract maximum list from max temprature column
        in file.

        Parameter
        ---------
        None
        
        Return
        ------
        None

        at the end list of max temp assign to class attribute list_of_max

        """
        temp = []
        row, col = 1,1
        for i in range(self.no_of_lines - 1):
            temp.append(self.file_data[row][col])
            row = row + 1
        self.list_of_max = temp
    
    def find_minimum_list_from_file(self):
        """
        This function is to extract minimum list from min temprature column
        in file.

        Parameter
        ---------
        None
        
        Return
        ------
        None

        at the end list of min temp assign to class attribute list_of_max
        """
        temp = []
        row,col = 1,3
        for i in range(self.no_of_lines - 1):
            temp.append(self.file_data[row][col])
            row = row + 1
        self.list_of_min = temp
        

    def convert_number_into_month(self,val):
        """
        convert month number to month name 
         
        Parameter
        ---------
        val : int
            Month number

        Return
        ------
        None    
        """
        switcher = {
            1:"Jan",
            2:"Feb",
            3:"Mar",
            4:"Apr",
            5:"May",
            6:"Jun",
            7:"Jul",
            8:"Aug",
            9:"Sep",
            10:"Oct",
            11:"Nov",
            12:"Dec"
        }
        self.month_name = switcher.get(val, "Invalid number of month")   

    def dsiplay_file_data(self):
        print(self.file_data)    
    #---------------- getter --------------------------    
    def get_max_list(self):
        '''return max_list stored in attribute'''
        return self.list_of_max

    def get_min_list(self):
        """return min_list which is stored in class attributes"""
        return self.list_of_min

    def get_whole_data_of_file(self):
        """return data which is read from file"""
        return self.file_data  

    def get_month(self):
        """return month name stored in attribute"""
        return self.month_name    

    def get_no_of_lines(self):
        """return number of rows in tuple stored in attribute"""
        return self.no_of_lines    