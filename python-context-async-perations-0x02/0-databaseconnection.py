import sqlite3

class DatabaseConnection:
    """Custom context manager for handling database connections"""
    
    def __init__(self, db_name):
        """Initialize with database name"""
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        """Enter the context - open database connection"""
        self.connection = sqlite3.connect(self.db_name)
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close database connection"""
        if self.connection:
            self.connection.close()
        # Return None to propagate any exceptions

# Use the context manager with the with statement
if __name__ == "__main__":
    # Use the context manager to perform a query
    with DatabaseConnection('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        
        print("Results from SELECT * FROM users:")
        for row in results:
            print(row)