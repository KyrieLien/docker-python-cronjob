import json
import pandas as pd
from datetime import datetime
import logging
from imp import reload 
from sqlalchemy import create_engine
# Opening JSON file
f = open("./posts.json", encoding="utf-8")
   
# returns JSON object as 
# a dictionary
data = json.load(f)
df = pd.DataFrame(data)

reload(logging)
FORMAT = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
# logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
    #   filename='./myapp.log',
    #   filemode='w')

logging.debug("Debug message")
logging.info("Informative message")
logging.warning('Protocol problem: %s', 'connection reset')
logging.error("Error message")

df1 = df[['title','createdAt', 'media', 'categories', 'excerpt', 'topics']]
df1['createdAt'] = pd.to_datetime(df1['createdAt'], format = '%Y-%m-%d %H:%M:%S' )
max_date = df1['createdAt'][0]
date_str = max_date.strftime("%Y-%m-%d %H:%M:%S")
df2 = df1.applymap(str)


engine = create_engine('sqlite://', echo=False)
df2.to_sql('users', con=engine, if_exists='append')
with engine.connect() as connection:
    result = connection.execute("SELECT * FROM users where createdAt < ?",  date_str)
    for r in result.fetchall():
        print(r)