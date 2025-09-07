#!/usr/bin/env python3
"""
Batch processing module with generators.

This module provides functions to fetch and process user data in batches
using generators, specifically filtering users over the age of 25.
"""

import seed


def stream_users_in_batches(batch_size):
    """
    Generator function that fetches rows in batches from the user_data table.
    
    Args:
        batch_size (int): Number of rows to fetch per batch
        
    Yields:
        list: A list of dictionaries containing user data for each batch
    """
    connection = seed.connect_to_prodev()
    
    if not connection:
        return
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT user_id, name, email, age FROM user_data")
        
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
            
    except Exception as e:
        print(f"Error streaming users in batches: {e}")
        
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def batch_processing(batch_size):
    """
    Processes each batch to filter users over the age of 25.
    
    Args:
        batch_size (int): Size of each batch to process
        
    Prints each filtered user that is over 25 years old.
    """
    # Loop 1: Iterate through batches
    for batch in stream_users_in_batches(batch_size):
        # Loop 2: Filter users in current batch
        filtered_users = []
        for user in batch:
            if user['age'] > 25:
                filtered_users.append(user)
        
        # Loop 3: Print filtered users
        for user in filtered_users:
            print(user)


if __name__ == "__main__":
    # Test the batch processing
    print("Testing batch processing with batch size of 10:")
    try:
        batch_processing(10)
    except Exception as e:
        print(f"Error in batch processing: {e}")
