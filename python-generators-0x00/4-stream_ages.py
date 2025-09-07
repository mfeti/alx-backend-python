#!/usr/bin/env python3
"""
Memory-efficient aggregation module using generators.

This module provides generator functions to compute aggregate functions
like average age for large datasets without loading all data into memory.
"""

import seed


def stream_user_ages():
    """
    Generator function that yields user ages one by one from the database.
    
    This is memory-efficient as it processes one record at a time instead
    of loading the entire dataset into memory.
    
    Yields:
        int: User age from the database
    """
    connection = seed.connect_to_prodev()
    
    if not connection:
        return
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")
        
        # Loop 1: Fetch and yield ages one by one
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            yield row[0]  # row[0] contains the age value
            
    except Exception as e:
        print(f"Error streaming user ages: {e}")
        
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def calculate_average_age():
    """
    Calculates the average age of users using the stream_user_ages generator.
    
    This function computes the average without loading the entire dataset
    into memory, making it very memory-efficient for large datasets.
    
    Returns:
        float: The average age of all users
    """
    total_age = 0
    count = 0
    
    # Loop 2: Process each age from the generator
    for age in stream_user_ages():
        total_age += age
        count += 1
    
    if count == 0:
        return 0
    
    return total_age / count


if __name__ == "__main__":
    # Calculate and print the average age
    try:
        average_age = calculate_average_age()
        print(f"Average age of users: {average_age:.2f}")
        
        # Additional testing: show some individual ages
        print("\nFirst 10 user ages:")
        age_count = 0
        for age in stream_user_ages():
            print(f"Age: {age}")
            age_count += 1
            if age_count >= 10:
                break
                
    except Exception as e:
        print(f"Error calculating average age: {e}")
