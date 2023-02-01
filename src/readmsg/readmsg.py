from rosbags.rosbag2 import Reader
from rosbags.serde import deserialize_cdr
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from commands.get import CommandsArg

def ReadMsg():
    args = CommandsArg()
    rosbag_path = args.get_rosbag()
    rosbag_title = ["topic", "timestamp", "message_type", "raw_data", 'msg']
    rosbag_list = []
    with Reader(rosbag_path) as reader:
        for connection, timestamp, rawdata in reader.messages():
            try: 
                msg = deserialize_cdr(rawdata, connection.msgtype)
            except:
                msg = None
            rosbag_list.append([
                connection.topic, 
                timestamp,
                connection.msgtype,
                rawdata,
                msg
            ])

    return rosbag_list, rosbag_title