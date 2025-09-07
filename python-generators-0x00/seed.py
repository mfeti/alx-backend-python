#!/usr/bin/env python3
"""
Database seeding module for ALX_prodev database.

This module provides functions to set up MySQL database, create tables,
and populate them with user data from CSV file.
"""

import mysql.connector
import csv
import uuid
from mysql.connector import Error


def connect_db():
    """
    Connects to the MySQL database server.
    
    Returns:
        connection: MySQL connection object or None if connection fails
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Change as needed
            password='',  # Change as needed
        )
        if connection.is_connected():
            print("Successfully connected to MySQL server")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None


def create_database(connection):
    """
    Creates the database ALX_prodev if it does not exist.
    
    Args:
        connection: MySQL connection object
    """
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created successfully or already exists")
        cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")


def connect_to_prodev():
    """
    Connects to the ALX_prodev database in MySQL.
    
    Returns:
        connection: MySQL connection object or None if connection fails
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Change as needed
            password='',  # Change as needed
            database='ALX_prodev'
        )
        if connection.is_connected():
            print("Successfully connected to ALX_prodev database")
            return connection
    except Error as e:
        print(f"Error while connecting to ALX_prodev database: {e}")
        return None


def create_table(connection):
    """
    Creates a table user_data if it does not exist with the required fields.
    
    Args:
        connection: MySQL connection object
    """
    try:
        cursor = connection.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3,0) NOT NULL,
            INDEX idx_user_id (user_id)
        )
        """
        
        cursor.execute(create_table_query)
        connection.commit()
        print("Table user_data created successfully")
        cursor.close()
        
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, csv_file):
    """
    Inserts data from CSV file into the database if it does not exist.
    
    Args:
        connection: MySQL connection object
        csv_file: Path to the CSV file containing user data
    """
    try:
        cursor = connection.cursor()
        
        # Check if data already exists
        cursor.execute("SELECT COUNT(*) FROM user_data")
        count = cursor.fetchone()[0]
        
        if count > 0:
            print(f"Data already exists in table ({count} records). Skipping insertion.")
            cursor.close()
            return
        
        # Read and insert data from CSV
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            insert_query = """
            INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
            """
            
            data_to_insert = []
            for row in csv_reader:
                # Validate UUID format (basic check)
                user_id = row['user_id'].strip()
                name = row['name'].strip()
                email = row['email'].strip()
                age = int(row['age'].strip())
                
                data_to_insert.append((user_id, name, email, age))
            
            # Insert all data
            cursor.executemany(insert_query, data_to_insert)
            connection.commit()
            
            print(f"Successfully inserted {len(data_to_insert)} records into user_data table")
        
        cursor.close()
        
    except Error as e:
        print(f"Error inserting data: {e}")
        connection.rollback()
    except FileNotFoundError:
        print(f"CSV file '{csv_file}' not found")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    # Test the functions
    connection = connect_db()
    if connection:
        create_database(connection)
        connection.close()
        
        # Connect to ALX_prodev database
        connection = connect_to_prodev()
        if connection:
            create_table(connection)
            insert_data(connection, 'user_data.csv')
            connection.close()
