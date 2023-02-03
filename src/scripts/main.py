import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from format.format import RosbagToFile

from commands.get import CommandsArg

if __name__ == '__main__':
    format = CommandsArg().get_format()
    RosbagToFile(format)

        


