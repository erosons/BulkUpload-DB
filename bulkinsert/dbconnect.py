import pyodbc


def conn():
    server = 'DESKTOP-SAMSON'
    database = 'AdventureWorks2019'
    username = "DESKTOP-SAMSON'\'gw"
    password = ''
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD='+password)

    return cnxn


def conn2():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-SAMSON;'
                          'Database=AdventureWorks2019;'
                          'Trusted_Connection=yes;')
    return conn
