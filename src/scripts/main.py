import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from format.rosbagTofile import RosbagToFile

from commands.get import CommandsArg

if __name__ == '__main__':
    args = CommandsArg()
    format = args.get_format()
    if format == 'json' :
        pass
    elif format == 'csv':
        rosbagToCsv = RosbagToFile(format=format)
        


