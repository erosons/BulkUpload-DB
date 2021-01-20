SqlCommand = """

use Credit

BULK INSERT [BULKS]
from 'C:/Users/gw/Documents/bulk_to insert.csv'
with
(
FIELDTERMINATOR = ','
,ROWTERMINATOR = '\n'
)

"""
