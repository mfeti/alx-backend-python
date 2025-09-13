import sqlite3

class ExecuteQuery:
    """Reusable context manager for executing database queries"""
    
    def __init__(self, db_name, query, params=None):
        """Initialize with database name, query, and optional parameters"""
        self.db_name = db_name
        self.query = query
        self.params = params or ()
        self.connection = None
        self.cursor = None
        self.results = None
    
    def __enter__(self):
        """Enter the context - open connection, execute query, and return results"""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        
        # Execute query with parameters if provided
        if self.params:
            self.cursor.execute(self.query, self.params)
        else:
            self.cursor.execute(self.query)
        
        # Fetch all results
        self.results = self.cursor.fetchall()
        return self.results
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close cursor and connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        # Return None to propagate any exceptions

# Use the context manager to execute the specified query
if __name__ == "__main__":
    # Execute query: "SELECT * FROM users WHERE age > ?" with parameter 25
    query = "SELECT * FROM users WHERE age > ?"
    param = (25,)
    
    with ExecuteQuery('database.db', query, param) as results:
        print(f"Results from query: {query} with parameter {param[0]}")
        print("Users older than 25:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
    
    print("\n" + "="*50)
    
    # Additional example: Get all users
    with ExecuteQuery('database.db', "SELECT * FROM users") as results:
        print("\nAll users:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")