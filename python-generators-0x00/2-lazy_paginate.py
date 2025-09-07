#!/usr/bin/env python3
"""
Lazy loading pagination module.

This module provides a generator function to lazily load paginated user data
from the database, fetching only the next page when needed.
"""

import seed


def paginate_users(page_size, offset):
    """
    Fetches a specific page of user data from the database.
    
    Args:
        page_size (int): Number of users per page
        offset (int): Number of records to skip
        
    Returns:
        list: List of dictionaries containing user data for the page
    """
    connection = seed.connect_to_prodev()
    
    if not connection:
        return []
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
        rows = cursor.fetchall()
        return rows
        
    except Exception as e:
        print(f"Error paginating users: {e}")
        return []
        
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def lazy_paginate(page_size):
    """
    Generator function that implements lazy loading pagination.
    
    This function fetches pages of user data on demand, only loading the next
    page when it's actually needed.
    
    Args:
        page_size (int): Number of users per page
        
    Yields:
        list: A list of dictionaries containing user data for each page
    """
    offset = 0
    
    while True:
        page_data = paginate_users(page_size, offset)
        
        # If no more data is returned, stop the generator
        if not page_data:
            break
            
        yield page_data
        offset += page_size


if __name__ == "__main__":
    # Test the lazy pagination
    print("Testing lazy pagination with page size of 5:")
    page_count = 0
    
    try:
        for page in lazy_paginate(5):
            page_count += 1
            print(f"\n--- Page {page_count} ---")
            for user in page:
                print(user)
            
            # Only show first 3 pages for testing
            if page_count >= 3:
                break
                
    except Exception as e:
        print(f"Error in lazy pagination: {e}")
