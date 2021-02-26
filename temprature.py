class Temprature:
    """
    A class temprature is repesent final data of report and update 
    data according parameter values.
    ...
    Attributes
    ----------  
    maximum_temprature : int 
        max temperature in month
    minimum_temprature : int 
        min temperature in month
    humidity : int
        humidity in month  
    day_of_max : int
        day of max temperature
    day_of_min : int
        day of min temperature
    day_of_humidity : int 
        day of max humidity 
    month_of_max : str
        month name of max temprature
    month_of_min : str
        month name of min temprature 
    month_of_humidity : str
        month name of max humidity    
    no_of_lines : int 
        no of rows in column


    Methods
    -------
    __init__(self): 
    set_maximum_average(self,val):
        set maximum_average with val  
    set_minimum_average(self,val):
        set minimum_average with val  
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
        maximum_temprature : int 
            max temperature in month
        minimum_temprature : int 
            min temperature in month
        humidity : int
            humidity in month  
        day_of_max : int
            day of max temperature
        day_of_min : int
            day of min temperature
        day_of_humidity : int 
            day of max humidity 
        month_of_max : str
            month name of max temprature
        month_of_min : str
            month name of min temprature 
        month_of_humidity : str
            month name of max humidity    
        no_of_lines : int 
            no of rows in column
       
        Return
        ------
        None     
        """
        self.maximum_temprature = 0
        self.minimum_temprature = 100
        self.humidity = 0
        self.day_of_max = 0
        self.day_of_min = 0
        self.day_of_humidity = 0
        self.month_of_max = "no month"
        self.month_of_min = "no month"
        self.month_of_humidity = "no month"

    def set_maximum(self,val,month,day):
        """
        set and update maximum value, month and day if parameter 
        value is greater than maximum_temperature.

        Parameter
        ---------
        val : int
            value
        month : str
            month name
        day : int 
            day value

        Return
        ------
        None    
        """    
        if(val.isdigit()):
            if int(val) > int(self.maximum_temprature):
                self.maximum_temprature = val
                self.month_of_max = month
                self.day_of_max = day

    def set_minimum(self,val,month,day):
        """
        set and update minimum value, month and day if parameter 
        value is less than minimum_temperature.

        Parameter
        ---------
        val : int
            value
        month : str
            month name
        day : int 
            day value

        Return
        ------
        None    
        """ 
        if(val.isdigit()):
            if int(val) < int(self.minimum_temprature):
                self.minimum_temprature = val
                self.month_of_min = month
                self.day_of_min = day

    def set_humidity(self,val,month,day):
        """
        set and update humidity value, month and day if parameter 
        value is greater than humidity.

        Parameter
        ---------
        val : int
            value
        month : str
            month name
        day : int 
            day value

        Return
        ------
        None    
        """ 
        self.humidity = val
        self.month_of_humidity = month
        self.day_of_humidity = day

    def display_report(self):
        ''' Print report '''
        print("Highest:",str(self.maximum_temprature) + "C","on", self.month_of_max, int(self.day_of_max))
        print("Lowest:",str(self.minimum_temprature) + "C","on", self.month_of_min, int(self.day_of_min))
        print("Humid:",str(self.humidity) + "%", "on", self.month_of_humidity,int(self.day_of_humidity))
