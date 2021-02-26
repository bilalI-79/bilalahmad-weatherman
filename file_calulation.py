class File:
    """
    A class to represent the file related work. or extract required data
    from file.
    ...
    Attributes
    ----------
    value_max : float
        max value of file
    value_min : float
        min value of file
    value_humid : float
        humid value of file
    day_max : int
        day of max value
    day_min : int 
        day of min value
    day_humid : int
        day of humid   
    no_of_line : int
        no of rows in column
    file_data = string
        whole data of file  

    Methods
    -------
    change_file_into_readable(self, file_pointer):
        read the file and return in the form of list  
    find_maximum_from_current_file(self): 
        extract max value from max temprature column and day also
    find_minimum_from_current_file(self): 
        extract min value from min temprature column and day also
    find_humidity_from_current_file(self):
        extract humidity value with day     
    dsiplay_file_data(self):
        print file data   
    get_max_value(self):
        return max_value    
    get_min_value(self):
        retune min_value
    get_humid_value(self):
        retune humid_value    
    get_whole_data_of_file(self):   
        return alll the data of file
    get_no_of_lines(self):
        return no of rows in column    
    """
    def __init__(self):
        """
        Construct all the necessary attributes for the file data

        Parameters
        ----------
        value_max : float
            max value of file
        value_min : float
            min value of file
        value_humid : float
            humid value of file
        day_max : int
            day of max value
        day_min : int 
            day of min value
        day_humid : int
            day of humid   
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
        self.value_max = 0
        self.value_min = 0
        self.value_humid = 0
        self.day_max = 0
        self.day_min = 0
        self.day_humid = 0
        self.no_of_lines = 0
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

    def find_maximum_from_current_file(self):
        """
        This function is to extract maximum list from max temprature column
        in file.and find max value.

        Parameter
        ---------
        None
        
        Return
        ------
        None

        at the end max of temprature assign to class attribute max_value
        and day to max_day

        """
        temp = []
        row, col = 1,1
        for i in range(self.no_of_lines - 1):
            temp.append(self.file_data[row][col])
            row = row + 1
        max_value = max(temp)
        max_index = temp.index(max_value)
        self.value_max = max_value
        self.day_max = max_index

    def find_minimum_from_current_file(self):
        """
        This function is to extract minimum list from min temprature column
        in file.and find min value.

        Parameter
        ---------
        None
        
        Return
        ------
        None

        at the end min of temprature assign to class attribute min_value
        and day to min_day

        """
        temp = []
        row,col = 1,3
        for i in range(self.no_of_lines - 1):
            temp.append(self.file_data[row][col])
            row = row + 1
        min_value = min(temp)
        min_index = temp.index(min_value)
        self.value_min = min_value
        self.day_min = min_index

    def find_humidity_from_current_file(self):
        """
        This function is to extract humidity list from  column
        in file.and find max humidty value.

        Parameter
        ---------
        None
        
        Return
        ------
        None

        at the end max of humidity assign to class attribute humidity_value
        and day to humid_day

        """
        temp = []
        row, col = 1,7
        for i in range(self.no_of_lines - 1):
            temp.append(self.file_data[row][col])
            row = row + 1
        max_value = max(temp)
        max_index = temp.index(max_value)
        self.value_humid = max_value
        self.day_humid = max_index

    def dsiplay_file_data(self):
        '''Print file data '''
        print(self.file_data)    
    #---------------- getter --------------------------    
    def get_max_value(self):
        '''return max value in current file'''
        return self.value_max

    def get_min_value(self):
        ''' Return min value int current file'''
        return self.value_min

    def get_humid_value(self):
        '''Return humidty value in current file'''
        return self.value_humid 

    def get_max_day(self):
        ''' return day of max temprature of current file'''
        return self.day_max

    def get_min_day(self):
        ''' return day of min temprature of current file'''
        return self.day_min

    def get_humid_day(self):
        ''' return day of humidity temprature of current file'''
        return self.day_humid

    def get_whole_data_of_file(self):
        ''' return data of current file'''
        return self.file_data             
