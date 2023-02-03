import sys
import os
import csv
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from read_rosbag.read_rosbag import read_rosbag
from commands.get import CommandsArg

class RosbagToFile:
    def __init__(self, format):
        self.format = format
        self.rosbag_path = CommandsArg().get_rosbag()
        self.rosbag_data_list, self.rosbag_csv_title = read_rosbag()
        self.datetime = datetime.today().strftime("%Y_%m_%d-%H_%M_%S")
        self.select_format()
    
    def create_csv_file(self, file_name):
        print('creating csv')

        with open(self.rosbag_path+"/"+file_name+'.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(self.rosbag_csv_title)
            writer.writerows(self.rosbag_data_list)

    def create_json_file(self, file_name):
        print('creating json')

    def select_format(self):
        if self.format == 'json' :
            self.create_json_file(self.select_file_name(self.format))
        elif self.format == 'csv' :
            self.create_csv_file(self.select_file_name(self.format))

    def select_file_name(self, format):
        file_naem = 'rosTo' + format.capitalize() + self.datetime
        
        return file_naem
        
        

