# rosbagTo
- rosbagToJson
- rosbagToCsv ...

### Install 
```
pip3 install -r requirements.txt
```

### Run 
```
python src/scripts/main.py --rosbag=../../test/data/rosbag2_2023_02_01-17_05_01/ --format=csv 
```

### Help command
```
python src/scripts/main.py -h
usage: main.py [-h] [--rosbag ROSBAG] [--format FORMAT]

rosbagTo

options:
  -h, --help       show this help message and exit
  --rosbag ROSBAG  bag directory path ex."/home/rosbag/"
  --format FORMAT  ouput file format -> "csv | json"
```
