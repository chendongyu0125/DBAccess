import pandas as pd
import pymysql
from sqlalchemy import create_engine
from bs4 import BeautifulSoup as bs
from nltk.tokenize import RegexpTokenizer as rt
import numpy as np
e=create_engine("mysql+pymysql://chendongyu:1234@localhost/ppdai?charset=utf8")

member=pd.read_sql_table("member",e)
print(member.columns)
