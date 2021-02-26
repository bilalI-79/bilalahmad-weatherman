class Temprature:
    """
    A class temprature is repesent final data of report and update 
    data according parameter values.
    ...
    Attributes
    ----------  
    maximum_temprature : float
        max avg in file
    minmum_tempratue : float
        min avg in file
    no_of_lines : float
        no of orws in column

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
        maximum_temprature : float
            max avg in file
        minmum_tempratue : float
            min avg in file
        humidity : float
            humid avg in column    
        no_of_lines : int
            no of orws in column
       
        Return
        ------
        None     
        """
        self.maximum_temprature = 0
        self.minimum_temprature = 0
        self.humidity = 0

    def set_maximum_average(self,val):
        """
        set maximum_average with val(val is the list of max average).

        Parameter
        ---------
        val : string
            average of max temprature 

        Return:
        None

        """
        self.maximum_temprature = val

    def set_minimum_average(self,val):
        """
        set minimum_average with val(val is the list of min average).

        Parameter
        ---------
        val : string
            average of min temprature 

        Return:
        None

        """
        self.minimum_temprature = val

    def set_humidity_average(self,val):
        """
        set humid_average with val(val is the list of max average).

        Parameter
        ---------
        val : string
            average of humidity 

        Return:
        None

        """
        self.humidity = val

    def display_report(self):
        ''' Print repot '''
        print("Highest Average:",str(self.maximum_temprature) + "C")
        print("Lowest Average:",str(self.minimum_temprature) + "C")
        print("Average Humidity:",str(self.humidity) + "%")
