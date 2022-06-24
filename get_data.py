import MySQLdb
import pandas as pd

try:
    db_connection = MySQLdb.connect("bjpm1nw3h1yvq88rsybl-mysql.services.clever-cloud.com", "uvuy3aoryk4jnwx0", "RYpyOl9JhGEKc3DIY3OM", "bjpm1nw3h1yvq88rsybl")
    print("Success connect to database")
except:
    print("Cant't connect to database")

def get_data(table_name):
    data = pd.read_sql_query("SELECT * FROM " + table_name, db_connection)
    return data