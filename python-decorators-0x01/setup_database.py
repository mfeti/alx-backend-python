#!/usr/bin/env python3
"""
Script to set up the SQLite database with users table and sample data
"""

import sqlite3

def setup_database():
    """Create users.db with users table and sample data"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    
    # Insert sample data
    sample_users = [
        ('Alice Johnson', 'alice.johnson@email.com'),
        ('Bob Smith', 'bob.smith@email.com'),
        ('Charlie Brown', 'charlie.brown@email.com'),
        ('Diana Prince', 'diana.prince@email.com'),
        ('Edward Wilson', 'edward.wilson@email.com')
    ]
    
    cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', sample_users)
    
    conn.commit()
    conn.close()
    print("Database setup completed successfully!")
    print("Created users.db with users table and sample data")

if __name__ == "__main__":
    setup_database()