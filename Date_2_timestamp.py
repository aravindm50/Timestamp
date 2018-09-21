import pandas as pd
import datetime
import time
import re
timee = []
df = pd.read_csv('file', sep = ',')
for i in df['Date Time']:
    x = re.split(' ',i)
    y = x[0].split('/')
    z = x[1].split(':')
    dt = datetime.datetime(int(y[2]), int(y[1]), int(y[0]), int(z[0]), int(z[1]))
    timee.append(time.mktime(dt.timetuple()))
    #print(timee)
csv_input = pd.read_csv('Aeroqual_CO_O3.csv')
csv_input['Timestamp'] = timee
csv_input.to_csv('output.csv', index=False)
