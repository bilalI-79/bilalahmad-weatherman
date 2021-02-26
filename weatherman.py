import argparse
from glob import glob
import temprature
import file_calulation


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("year", help = "enter year")
    parser.add_argument("path", help = "enter path")
    args = parser.parse_args()
    path = args.path
    file_names = glob(path + '/*.*')
    year = int(args.year)
    data_extraction = file_calulation.File()
    create_report = temprature.Temprature()
    
    file_number=0
    for i in file_names:
        extract_required_file = file_names[file_number]
        total_len = len(extract_required_file)
        year_number = extract_required_file[(total_len - 12):(total_len - 8)]
        month_of_year = extract_required_file[(total_len - 7):(total_len - 4)]
        if(int(year_number) == year):
            file_point = open(extract_required_file, "r")
            """
            required data extraction from  current file by file_calculation object
            """ 
            data_extraction.change_file_into_readable(file_point)
            data_extraction.find_maximum_from_current_file()
            data_extraction.find_minimum_from_current_file()
            data_extraction.find_humidity_from_current_file()

            """
            Insert requied  current file data to temprature object for
            creating report
            """
            create_report.set_maximum(data_extraction.get_max_value(),month_of_year
            ,data_extraction.get_max_day())
            create_report.set_minimum(data_extraction.get_min_value(),month_of_year
            ,data_extraction.get_min_day())
            create_report.set_humidity(data_extraction.get_humid_value(),month_of_year
            ,(data_extraction.get_humid_day() + 1))

            file_point.close()
            
        file_number = file_number + 1
    create_report.display_report()    

   