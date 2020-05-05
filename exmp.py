from pyhive import hive
import pandas as pd

conn = hive.Connection(host="localhost", port=10000,     username="hduser",database="employee", auth="NOSASL")

df = pd.read_sql('select * from details',conn)
print(df)


