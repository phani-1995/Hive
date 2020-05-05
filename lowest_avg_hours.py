from pyhive import hive
import pandas as pd
import sys
#Establish the connection between hive server and Database
conn = hive.Connection(host="localhost", port=10000, database="logs", auth="NOSASL")

#load database into hive
query= pd.read_sql('select * from cpulogs', conn)
#convert the data into the format of datetime
query['cpulogs.working_hours'] = pd.to_datetime(query['cpulogs.working_hours'])
#calculate the mean of total working_hours
avghour = query[query['cpulogs.working_hours'] < query['cpulogs.working_hours'].mean()]
print(avghour)
#print the user_name with lowest average hours
LOWEST_AVG_HOURS =avghour['cpulogs.user_name']
print(LOWEST_AVG_HOURS)
