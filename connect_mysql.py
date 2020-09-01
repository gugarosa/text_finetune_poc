from utils.mysql import Session

# Creates a MySQL session
db = Session()

# Defines a query
query = 'SELECT * from qeztn_normas_area'

# Executes the query
db.cursor.execute(query)

# Iterates over the query results
for row in db.cursor:
    print(row)

# Closes the MySQL session
db.close()
