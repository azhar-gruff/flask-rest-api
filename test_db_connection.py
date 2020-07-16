import pyodbc
#import pymssql
from sqlalchemy import create_engine
import urllib
import os


SQLALCHEMY_DATABASE_URI = os.environ.get('SQLAZURECONNSTR_WWIF')

#params = urllib.parse.quote_plus(SQLALCHEMY_DATABASE_URI)
params = urllib.parse.quote_plus('Driver={ODBC Driver 17 for SQL Server};Server=tcp:sbkk-edb-sqldb-api-dev.database.windows.net,1433;Database=sbkk_Azure_sqldb_dev;Uid=sbkkadmin;Pwd=1qaz!QAZ;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30')
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
#conn_str = 'mssql+pymssql://sbkkadmin:qaz!QAZ@sbkk-edb-sqldb-api-dev.database.windows.net:1433/sbkk_Azure_sqldb_dev'
engine_azure = create_engine(conn_str,echo=True)

print('connection is ok')
print(engine_azure.table_names())

#reverse engineer mssql schema 
#flask-sqlacodegen --schema company --noviews --outfile models.py 'mssql+pyodbc://sbkkadmin:1qaz!QAZ@sbkk-edb-sqldb-api-dev.database.windows.net:1433/sbkk_Azure_sqldb_dev?driver=ODBC+Driver+17+for+SQL+Server'
