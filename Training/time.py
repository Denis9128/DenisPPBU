from pip._internal.utils import datetime
from time import time
from datetime import datetime

now = datetime.now()
current_time = now.today()
time_tek = current_time.strftime("%H:%M:%S")
print(time_tek)