import avg
class File:
    """
    A class to represent the file related work. or extract required data
    from file.
    ...
    Attributes
    ----------
    avg_max : float
        store of average of max in list
    avg_min : float
        store of average of min in list
    avg_humid : float
        store of average of humid in list    
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
    find_maximum_avg_from_file(self): 
        extract max avg from max temprature column
    find_minimum_avg_from_file(self):
        extract min avg from min temprature column
    find_humidity_avg_from_file(self):
        extract humidity average     
    convert_number_into_month(self,val):
        return month name  
    dsiplay_file_data(self):
        print file data   
    get_max_avg(self):
        return max_avg    
    get_min_avg(self):
        retune min_avg
    get_humid_avg(self):
        retune humid_avg    
    get_whole_data_of_file(self):   
        return alll the data of file
    get_month(self):         
        return month name
    get_no_of_lines(self):
        return no of rows in column    
    """
    def __init__(self):
        """
        Construct all the necessary attributes for the file data

        Parameters
        ----------
        avg_max : float
            store of average of max in list
        avg_min : float
            store of average of min in list
        avg_humid : float
            store of average of humid in list    
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
        self.avg_max = 0
        self.avg_min = 0
        self.avg_humid = 0
        self.no_of_lines = 0
        self.file_data = []
        self.month_name="no month"
 
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

    

    def find_maximum_avg_from_file(self):
        """
        This function is to extract maximum list from max temprature column
        in file.and find max avg by using avg object

        Parameter
        ---------
        None
        
        Return
        ------
        None

        at the end average of temprature assign to class attribute avg_max

        """
        temp = []
        row, col = 1,1
        for i in range(self.no_of_lines - 1):
            temp.append(self.file_data[row][col])
            row = row + 1
        avg_inst = avg.Average()
        self.avg_max = avg_inst.find_avarage(temp, self.no_of_lines)


    def find_minimum_avg_from_file(self):
        """
        This function is to extract minimum list from min temprature column
        in file.and find min avg by using avg object

        Parameter
        ---------
        None
        
        Return
        ------
        None

        at the end average of temprature assign to class attribute avg_min

        """
        temp = []
        row,col = 1,3
        for i in range(self.no_of_lines - 1):
            temp.append(self.file_data[row][col])
            row = row + 1
        avg_inst=avg.Average()
        self.avg_min = avg_inst.find_avarage(temp, self.no_of_lines)    

    def find_humidity_avg_from_file(self):
        """
        This function is to extract humidity list
        in file.and find humidty avg by using avg object

        Parameter
        ---------
        None
        
        Return
        ------
        None

        at the end average of temprature assign to class attribute avg_humid

        """
        temp = []
        row, col = 1,7
        for i in range(self.no_of_lines - 1):
            temp.append(self.file_data[row][col])
            row = row + 1
        avg_inst = avg.Average()
        self.avg_humid = avg_inst.find_avarage(temp, self.no_of_lines)    
        
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
    def get_max_avg(self):
        ''' return max avg '''
        return self.avg_max

    def get_min_avg(self):
        '''return min average '''
        return self.avg_min

    def get_humid_avg(self):
        ''' return humid avgerage '''
        return self.avg_humid 

    def get_whole_data_of_file(self):
        ''' return file data '''
        return self.file_data  
    def get_month(self):
        ''' return month nmae '''
        return self.month_name               
