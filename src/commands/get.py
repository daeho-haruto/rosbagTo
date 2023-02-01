import argparse


class CommandsArg:
    def __init__(self):
        parser = argparse.ArgumentParser(description="rosbagTo")
        parser.add_argument(
            '--rosbag', help='bag directory path ex."/home/rosbag/"')
        parser.add_argument('--format', help='ouput file format -> "csv | json"')
        self.args = parser.parse_args()

    def get_rosbag(self):
        return self.args.rosbag
    
    def get_format(self):
        return self.args.format
