from pyhive import hive
import pandas as pd
import sys
#Establish the connection between hive server and Database
conn = hive.Connection(host="localhost", port=10000, database="logs", auth="NOSASL")

try:
    #load database into hive
    query = pd.read_sql('select * from cpulogs', conn)
    #convert the data into the format of datetime
    query['cpulogs.idle_time'] = pd.to_datetime(query['cpulogs.idle_time'])
    #calculate total idle_hours mean
    idledata =query[query['cpulogs.idle_time'] >      query['cpulogs.idle_time'].mean()]
    print(idledata)
    #print user_name with HIGHEST_IDLE_HOURS
    HIGHEST_IDLE_HOURS=idledata['cpulogs.user_name']
    print(HIGHEST_IDLE_HOURS)
except:
    print("Syntax error")
