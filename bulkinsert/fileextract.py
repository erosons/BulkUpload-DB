import pydoc
import numpy as np
import pandas as pd
from script1 import Command
from bulkinsert import SqlCommand
from dbconnect import conn2


df = pd.read_sql_query(SqlCommand, conn2())
print(df.head(5))

"""
cursor = conn2().cursor()
cursor.execute(SqlCommand)
print("upload was successful")
"""
