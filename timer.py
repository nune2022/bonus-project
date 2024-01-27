import datetime
import time


st = input('Insert time to count down (h:m:s) ')
if int(st.split(':')[0]) > 23:
    raise Exception("Hour is too large. ENTER AN HOUR LESS THAN 24!!!")

h, m, s = 0, 0, 0
date_time_obj = datetime.datetime.strptime(st, '%H:%M:%S')

while True:
    if s > 59:
        s = 0
        m = m + 1
    if m > 59:
        m = 0
        h = h + 1
    l = datetime.datetime.strptime('{}:{}:{}'.format(h, m, s), '%H:%M:%S')
    if date_time_obj >= l:
        s += 1
        x = date_time_obj - l
        print(x)
        time.sleep(1)
    else:
        print('Time is over !')
        break
