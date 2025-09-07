#!/usr/bin/env python3
"""
Stream users generator module.

This module provides a generator function to fetch user data from the database
one row at a time using Python's yield functionality.
"""

import seed


def stream_users():
    """
    Generator function that fetches rows one by one from the user_data table.
    
    Yields:
        dict: A dictionary containing user data with keys: user_id, name, email, age
    """
    connection = seed.connect_to_prodev()
    
    if not connection:
        return
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT user_id, name, email, age FROM user_data")
        
        # Use fetchone() in a loop to get one row at a time
        # This is more memory efficient than fetchall()
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            yield row
            
    except Exception as e:
        print(f"Error streaming users: {e}")
        
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    # Test the generator
    print("Testing stream_users generator:")
    count = 0
    for user in stream_users():
        print(user)
        count += 1
        if count >= 5:  # Only show first 5 users for testing
            break
