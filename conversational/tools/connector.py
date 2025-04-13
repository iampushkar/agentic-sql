import mysql.connector

# Create a connection
connection = mysql.connector.connect(
    host="localhost",        # or 127.0.0.1
    port=3306,               # default MySQL port
    user="root",    # replace with your MySQL username
    password="Happiness@29",# replace with your MySQL password
    database="test_db"  # replace with your database name
)

cursor = connection.cursor()

def executeQuery(query: str):
   """
   Executes the SQL Query and return the response.

    Args:
        query: this is a MySQL query
        Example: SELECT * FROM test_db.charts
    Returns:
       A row or List or Rows. 
    """
   
   cursor.execute(query)
   results = cursor.fetchall()
   for row in results:
        print(row)
   return results


