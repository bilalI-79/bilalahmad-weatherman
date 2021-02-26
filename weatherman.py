import argparse
import temprature
import file_calulation


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("date", help = "enter date")
    parser.add_argument("path", help = "enter path")
    args = parser.parse_args()
    path = args.path
    date = args.date
    month_in_number = int(date[len(date)-1]) 
    year = int(date[0:4])
    data_extraction = file_calulation.File()
    create_report = temprature.Temprature()
    data_extraction.convert_number_into_month(month_in_number)
    file_point = open(path+"/Murree_weather_"+ str(year) +"_"
     + str(data_extraction.get_month()) + ".txt" , "r")
    """
    required data extraction from file by file_calculation object
    """ 
    data_extraction.change_file_into_readable(file_point)
    data_extraction.find_maximum_avg_from_file()
    data_extraction.find_minimum_avg_from_file()
    data_extraction.find_humidity_avg_from_file()
    """
    Insert requied data to temprature object for creating report
    """
    create_report.set_maximum_average(data_extraction.get_max_avg())
    create_report.set_minimum_average(data_extraction.get_min_avg())
    create_report.set_humidity_average(data_extraction.get_humid_avg())
    create_report.display_report()
