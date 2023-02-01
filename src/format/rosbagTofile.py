import sys
import os
import csv
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from readmsg.readmsg import ReadMsg
from commands.get import CommandsArg

class RosbagToFile:
    def __init__(self, format):
        args = CommandsArg()
        self.format = format
        self.rosbag_path = args.get_rosbag()
        self.rosbag_data_list, self.rosbag_csv_title = ReadMsg()
        self.select_format()
    
    def create_csv_file(self):
        file_naem = 'rosToCsv' + datetime.today().strftime("%Y_%m_%d-%H_%M_%S")
        print('creating csv')

        with open(self.rosbag_path+"/"+file_naem+'.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(self.rosbag_csv_title)
            writer.writerows(self.rosbag_data_list)

    def create_json_file(self):
        file_naem = 'rosToJson' + datetime.today().strftime("%Y_%m_%d-%H_%M_%S")
        print('creating json')

    def select_format(self):
        if self.format == 'json' :
            self.create_json_file()
        elif self.format == 'csv' :
            self.create_csv_file()

        
        

