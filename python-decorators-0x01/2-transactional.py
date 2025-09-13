import sqlite3 
import functools

def with_db_connection(func):
    """Decorator that handles database connection opening and closing"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            # Pass the connection as the first argument to the decorated function
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper

def transactional(func):
    """Decorator that manages database transactions with commit/rollback"""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            # Execute the function
            result = func(conn, *args, **kwargs)
            # If no exception occurred, commit the transaction
            conn.commit()
            return result
        except Exception as e:
            # If an exception occurred, rollback the transaction
            conn.rollback()
            print(f"Transaction failed. Rolling back. Error: {e}")
            raise  # Re-raise the exception
    return wrapper

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 

#### Update user's email with automatic transaction handling 
if __name__ == "__main__":
    try:
        update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
        print("User email updated successfully!")
        
        # Verify the update
        from sqlite3 import connect
        conn = connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = 1")
        user = cursor.fetchone()
        print(f"Updated user: {user}")
        conn.close()
    except Exception as e:
        print(f"Error updating user email: {e}")