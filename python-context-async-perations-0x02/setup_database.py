#!/usr/bin/env python3
"""
Script to set up the SQLite database with users table and sample data
for context manager and async operations tasks
"""

import sqlite3

def setup_database():
    """Create database.db with users table and sample data"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Create users table with age column for the tasks
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    
    # Clear existing data
    cursor.execute('DELETE FROM users')
    
    # Insert sample data with ages for testing
    sample_users = [
        ('Alice Johnson', 25),
        ('Bob Smith', 35),
        ('Charlie Brown', 45),
        ('Diana Prince', 30),
        ('Edward Wilson', 50),
        ('Fiona Green', 22),
        ('George White', 60),
        ('Helen Black', 28),
        ('Ivan Blue', 42),
        ('Jane Red', 38)
    ]
    
    cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', sample_users)
    
    conn.commit()
    conn.close()
    print("Database setup completed successfully!")
    print("Created database.db with users table and sample data")
    print("Users with various ages for testing context managers and async operations")

if __name__ == "__main__":
    setup_database()