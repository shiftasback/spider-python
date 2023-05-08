import pymysql
from sqlalchemy import create_engine
import pandas as pd
db = pymysql.connect(
      host='127.0.0.1',
      port=3306,
      user='root',
      passwd='',
      db='pytest',
      charset='utf8')
cursor = db.cursor()
engine = create_engine('mysql+pymysql://root:@localhost:3306/pytest')
df = pd.read_csv('C:/Users/Wintogo/PycharmProjects/spider/spider-python/spiderdataxiaoqu.csv', sep=',')
df.to_sql('mpg', engine, index= True)
