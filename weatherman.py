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
    split_date=date.split('/')
    month_in_number = int(split_date[1]) 
    year = int(split_date[0])
    data_extraction = file_calulation.File()
    create_report = temprature.Temprature()
    data_extraction.convert_number_into_month(month_in_number)
    file_point = open(path + "/Murree_weather_" + str(year) + "_"
     + str(data_extraction.get_month()) + ".txt" , "r")
    """
    required data extraction from file by file_calculation object
    """
    data_extraction.change_file_into_readable(file_point)
    data_extraction.find_maximum_list_from_file()
    data_extraction.find_minimum_list_from_file()
    
    """
    Insert requied data to temrature object for creating proccess
    """
    create_report.set_maximum_list(data_extraction.get_max_list())
    create_report.set_minimum_list(data_extraction.get_min_list())
    create_report.set_no_of_lines(data_extraction.get_no_of_lines())
    create_report.display_report()
