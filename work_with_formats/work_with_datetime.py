import datetime
import time

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

current_time = datetime.datetime.now()
current_timestamp = current_time.timestamp()
in_str = current_time.strftime('%d.%m.%y %H:%M:%S')
in_datetime = datetime.datetime.strptime(in_str, '%d.%m.%y %H:%M:%S')

timestamp = time.time()
from_timestamp = datetime.datetime.fromtimestamp(timestamp)

if __name__ == '__main__':
    print(today, yesterday, tomorrow, sep='\n', end='\n\n')
    print(current_time, current_timestamp, in_str, in_datetime, sep='\n', end='\n\n')
    print(timestamp, from_timestamp, sep='\n', end='\n\n')